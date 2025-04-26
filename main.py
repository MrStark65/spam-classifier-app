import streamlit as st
import joblib

# Load the saved model and vectorizer
vectorizer, model = joblib.load('spam_classifier_pipeline.joblib')

# Streamlit app
st.title("📩 Spam Classifier App")
st.write("Enter a message below to predict if it's Spam or Ham.")

# Text input for the message
message = st.text_area("Message:", height=150)

if st.button("Predict"):
    if not message.strip():
        st.warning("Please enter a message to predict.")
    else:
        # Transform the message with the vectorizer and predict
        msg_vec = vectorizer.transform([message])
        pred = model.predict(msg_vec)[0]

        # Show the prediction
        result = '🚫 Spam' if pred == 1 else '✅ Ham'
        st.subheader(f"Prediction: {result}")
