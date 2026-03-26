# 📰 Fake News Detection

This project builds a machine learning model to classify news articles as **Fake** or **Real** using Natural Language Processing (NLP) techniques.

---

## 📌 Project Overview

- Clean and preprocess text data
- Convert text into numerical features using **TF-IDF**
- Train a classification model using **Logistic Regression**
- Evaluate model performance using multiple metrics
- Build a simple web app using **Streamlit**

---

## 📊 Dataset

- Fake news: `Fake.csv`
- Real news: `True.csv`
- Total: ~40,000+ news articles

---

## ⚙️ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit

---

## 🧠 Model

- Algorithm: Logistic Regression
- Feature extraction: TF-IDF (max_features=5000)

---

## 📈 Results

- Accuracy: ~98%
- Precision / Recall balanced across classes
- Evaluated using:
  - Confusion Matrix
  - Classification Report

---

## 🖥️ Demo (Streamlit App)

Run locally:

```bash
streamlit run app/streamlit_app.py