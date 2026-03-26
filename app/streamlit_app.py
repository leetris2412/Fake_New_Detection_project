import streamlit as st
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "..", "model", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "..", "model", "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

st.title("Fake News Detection")

text = st.text_area("Enter news")

if st.button("Predict"):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    
    if prediction[0] == 0:
        st.write("Fake News")
    else:
        st.write("Real News")