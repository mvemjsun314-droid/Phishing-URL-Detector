import streamlit as st
import pickle
import pandas as pd

from scipy.sparse import hstack, csr_matrix
from src.features import extract_url_features


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🛡️",
    layout="centered"
)


# --------------------------------------------------
# Load Model and Vectorizer
# --------------------------------------------------

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🛡️ Phishing URL Detector")

st.markdown(
    "Analyze a URL using **machine learning** and "
    "**URL-based security characteristics**."
)

st.divider()


# --------------------------------------------------
# URL Input
# --------------------------------------------------

st.subheader("🔗 Enter a URL")

url = st.text_input(
    "URL",
    placeholder="https://example.com",
    label_visibility="collapsed"
)

analyze = st.button(
    "🔍 Analyze URL",
    use_container_width=True
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if analyze:

    if not url.strip():

        st.warning("Please enter a URL.")

    else:

        # Extract structural features
        features = extract_url_features(url)

        # TF-IDF features
        tfidf_features = vectorizer.transform([url])

        # Structural features
        structural_df = pd.DataFrame([features])

        structural_matrix = csr_matrix(
            structural_df.values
        )

        # Combine both feature sets
        combined_features = hstack(
            [
                tfidf_features,
                structural_matrix
            ]
        )

        # Prediction
        prediction = model.predict(
            combined_features
        )[0]

        probabilities = model.predict_proba(
            combined_features
        )[0]

        confidence = max(probabilities) * 100


        # --------------------------------------------------
        # Result
        # --------------------------------------------------

        st.divider()

        st.subheader("📊 Analysis Result")

        if prediction == 0:

            st.error(
                "⚠️ This URL appears to be potentially phishing."
            )

        else:

            st.success(
                "✅ This URL appears to be legitimate."
            )


        st.metric(
            "Model Confidence",
            f"{confidence:.2f}%"
        )

        st.caption(
            "Model confidence represents the probability estimated "
            "for the selected classification. It is not a guarantee "
            "that a URL is safe or malicious."
        )


        # --------------------------------------------------
        # Security Analysis
        # --------------------------------------------------

        st.divider()

        st.subheader("🔎 URL Security Analysis")

        col1, col2 = st.columns(2)


        # Left column
        with col1:

            if features["IsHTTPS"]:

                st.success("🔒 HTTPS detected")

            else:

                st.warning("⚠️ HTTPS not detected")


            if features["IsDomainIP"]:

                st.warning("🌐 Domain is an IP address")

            else:

                st.success("🌐 Domain uses a hostname")


            if features["HasObfuscation"]:

                st.warning(
                    "⚠️ Possible URL obfuscation detected"
                )

            else:

                st.success(
                    "✅ No obvious URL obfuscation"
                )


        # Right column
        with col2:

            st.write(
                f"**URL length:** {features['URLLength']}"
            )

            st.write(
                f"**Domain length:** {features['DomainLength']}"
            )

            st.write(
                f"**Subdomains:** {features['NoOfSubDomain']}"
            )

            st.write(
                f"**Digits in URL:** {features['NoOfDegitsInURL']}"
            )

            st.write(
                f"**Query marks:** {features['NoOfQMarkInURL']}"
            )

            st.write(
                f"**Parameters (&):** "
                f"{features['NoOfAmpersandInURL']}"
            )


        # --------------------------------------------------
        # Footer Notice
        # --------------------------------------------------

        st.divider()

        st.info(
            "🛡️ This project provides an ML-based URL assessment "
            "for educational and demonstration purposes. "
            "Do not open suspicious URLs just to test them."
        )