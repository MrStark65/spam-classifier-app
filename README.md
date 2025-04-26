# 📩 Spam Classifier Streamlit App

A simple **Streamlit web app** that predicts whether a message is **Spam** or **Ham** (not spam) using a machine learning model trained on text data.

---

## 🚀 Features

- **Instant Classification:** Enter a message and classify it instantly as Spam or Ham.
- **Machine Learning Powered:** Uses a saved `TfidfVectorizer` and `Logistic Regression` model.
- **User-Friendly:** Clean, simple interface built with Streamlit.

---

## 🛠️ Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/yourusername/spam-classifier-streamlit.git
    cd spam-classifier-streamlit
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Ensure you have the following files in the root directory:**
    - `app.py` (the Streamlit app)
    - `vectorizer.pkl` (saved TfidfVectorizer)
    - `model.pkl` (saved Logistic Regression model)

---

## 🚦 Usage

Run the app locally:

streamlit run app.py


- Enter a message in the input box.
- Click **Predict** to see if it’s Spam or Ham.

---

## 📝 Example

Message: "Congratulations! You've won a free ticket."
Prediction: Spam 🎉

Message: "Hey, are we meeting for coffee today?"
Prediction: Ham ☕


---

## 📦 Requirements

- Python 3.7+
- Streamlit
- scikit-learn
- joblib or pickle

All dependencies are listed in `requirements.txt`.

---

## 🧠 Model Info

- **Vectorizer:** TfidfVectorizer (pre-trained and saved as `vectorizer.pkl`)
- **Classifier:** Logistic Regression (pre-trained and saved as `model.pkl`)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

[MIT](LICENSE)

---

## 🙋‍♂️ Acknowledgements

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- SMS Spam Collection Dataset

---

Happy classifying! 🚀
