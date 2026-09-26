import pandas as pd
import pickle

from scipy.sparse import hstack, csr_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

from features import extract_url_features


print("Loading dataset...")
df = pd.read_csv("data/phishing.csv")

print("Dataset shape:", df.shape)

df["URL"] = df["URL"].astype(str)
df["label"] = df["label"].astype(int)


# --------------------------------------------------
# Train / Test Split
# --------------------------------------------------

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

print("Training samples:", len(train_df))
print("Testing samples:", len(test_df))


# --------------------------------------------------
# 1. Character TF-IDF Features
# --------------------------------------------------

print("\nCreating TF-IDF features...")

vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(3, 5),
    min_df=2,
    max_features=100000
)

X_train_tfidf = vectorizer.fit_transform(train_df["URL"])
X_test_tfidf = vectorizer.transform(test_df["URL"])

print("TF-IDF training shape:", X_train_tfidf.shape)


# --------------------------------------------------
# 2. Structural URL Features
# --------------------------------------------------

print("\nExtracting structural URL features...")

train_structural = train_df["URL"].apply(extract_url_features)
test_structural = test_df["URL"].apply(extract_url_features)

X_train_structural = pd.DataFrame(
    train_structural.tolist()
)

X_test_structural = pd.DataFrame(
    test_structural.tolist()
)

print(
    "Structural feature shape:",
    X_train_structural.shape
)


# --------------------------------------------------
# Convert structural features to sparse format
# --------------------------------------------------

X_train_structural = csr_matrix(
    X_train_structural.values
)

X_test_structural = csr_matrix(
    X_test_structural.values
)


# --------------------------------------------------
# 3. Combine Both Feature Sets
# --------------------------------------------------

print("\nCombining TF-IDF + structural features...")

X_train = hstack(
    [X_train_tfidf, X_train_structural]
)

X_test = hstack(
    [X_test_tfidf, X_test_structural]
)

y_train = train_df["label"]
y_test = test_df["label"]

print("Final training feature shape:", X_train.shape)


# --------------------------------------------------
# 4. Train Model
# --------------------------------------------------

print("\nCreating Logistic Regression model...")

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

print("Training model...")

model.fit(X_train, y_train)


# --------------------------------------------------
# 5. Evaluate Model
# --------------------------------------------------

print("\nEvaluating model...")

predictions = model.predict(X_test)

print("\nModel Performance:")
print(
    classification_report(
        y_test,
        predictions
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        predictions
    )
)


# --------------------------------------------------
# 6. Save Model + Vectorizer
# --------------------------------------------------

print("\nSaving model...")

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

print("Model saved as model.pkl")
print("Vectorizer saved as vectorizer.pkl")