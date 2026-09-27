# 🛡️ Phishing URL Detector

A machine learning-based cybersecurity project that analyzes URLs and classifies them as **potentially phishing** or **legitimate**.

The project combines **character-level TF-IDF features** with **structural URL security features** and provides an interactive **Streamlit web application** for URL analysis.

> ⚠️ This project is intended for educational and demonstration purposes. It does not guarantee that a URL is safe or malicious.

---

## 🚀 Features

- 🔍 Phishing vs. legitimate URL classification
- 🤖 Machine learning-based detection
- 🔤 Character-level TF-IDF analysis
- 🌐 Structural URL feature analysis
- 🔒 HTTPS detection
- 🌐 IP-address domain detection
- ⚠️ URL obfuscation detection
- 📊 URL length and domain analysis
- 🔢 Special-character and digit analysis
- 📈 Model confidence display
- 🖥️ Interactive Streamlit interface

---

## 🧠 How It Works

The system analyzes a submitted URL using two types of features:

### 1. Character-Level TF-IDF Features

The URL is converted into character n-gram features using `TfidfVectorizer`.

This allows the model to learn patterns commonly associated with phishing and legitimate URLs.

### 2. Structural URL Features

The application extracts security-related characteristics such as:

- URL length
- Domain length
- Whether the domain is an IP address
- Number of subdomains
- Number of digits
- Number of query parameters
- Number of special characters
- HTTPS usage
- Possible URL obfuscation

These features are combined with the TF-IDF representation and passed to the trained classification model.

---

## 🤖 Machine Learning Model

The project uses:

- **TF-IDF Vectorization** for character-level URL representation
- **Logistic Regression** for classification
- **13 structural URL features**
- Sparse feature combination using `scipy.sparse.hstack`

The model was evaluated using a held-out test set from the dataset.

### Test Results

The hybrid model achieved approximately **99% accuracy on the held-out test set**.

Confusion matrix:

```text
[[20027   162]
 [    2 26968]]
```

> Important: Test-set performance does not guarantee the same performance on previously unseen real-world URLs. Dataset bias and domain generalization are important limitations of this project.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- Streamlit
- Pickle
- Git & GitHub

---

## 📂 Project Structure

```text
Phishing-URL-Detector/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── src/
│   ├── features.py
│   └── train.py
│
└── data/
    └── phishing.csv
```

> The dataset is excluded from the GitHub repository using `.gitignore` because of its size.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mvemjsun314-droid/Phishing-URL-Detector.git
cd Phishing-URL-Detector
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Dataset

This project uses the **PhiUSIIL Phishing URL Dataset** from the UCI Machine Learning Repository.

The dataset contains URL-based features for phishing and legitimate websites.

Dataset source:

**UCI Machine Learning Repository — PhiUSIIL Phishing URL Dataset**

The dataset is not included in this GitHub repository because the CSV file is approximately 57 MB.

---

## ▶️ Running the Application

After installing the dependencies, run:

```bash
streamlit run app.py
```

The application will open in your browser.

Enter a URL such as:

```text
https://google.com
```

and click:

**🔍 Analyze URL**

The application will display:

- Classification result
- Model confidence
- HTTPS status
- Domain type
- Possible obfuscation
- URL length
- Domain length
- Number of subdomains
- Number of digits
- Query marks
- URL parameters

---

## 🔎 Example

### Legitimate URL

```text
https://google.com
```

The model identifies the URL as:

```text
✅ This URL appears to be legitimate.
```

### Suspicious URL

```text
http://192.168.1.1/login.php?verify=account
```

The application can identify indicators such as:

- HTTP instead of HTTPS
- IP-address-based domain
- Login-related URL structure
- Query parameters

and classify the URL based on the learned model patterns.

---

## ⚠️ Limitations

This project has several limitations:

- Machine learning predictions are not guarantees.
- Dataset bias can affect model behavior.
- The model may perform differently on completely new domains.
- URL-only analysis cannot inspect the actual website content.
- The system does not perform live website reputation checks.
- Model confidence should not be interpreted as certainty.
- Suspicious URLs should not be opened simply for testing.

---

## 🔮 Future Improvements

Possible improvements include:

- Add domain reputation checks
- Integrate external threat-intelligence sources
- Add DNS and WHOIS-based features
- Analyze webpage content
- Add URL shortening detection
- Improve detection of previously unseen domains
- Add explainable AI features
- Create automated model evaluation pipelines
- Deploy the application as a cloud-based security tool

---

## 📌 Project Purpose

This project was developed as a hands-on cybersecurity and machine learning project to understand:

- Phishing detection
- URL-based threat analysis
- Feature engineering
- Machine learning classification
- Model evaluation
- Python development
- Streamlit application development
- Git and GitHub project management

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**.

The prediction generated by the model should not be treated as a definitive security verdict. Always use appropriate security tools and threat-intelligence sources when evaluating potentially malicious URLs.
