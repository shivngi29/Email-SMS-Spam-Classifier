import streamlit as st
import pickle
from helper import transform_text
tfif = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))
st.title("Email/SMS Spam Classifier")
input_sms = st.text_area("Enter the message")
if st.button("Predict"):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)

    # 2. Vectorize
    vector_input = tfif.transform([transformed_sms])

    # 3. Predict
    result = model.predict(vector_input)

    # 4. Display
    if result[0] == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")