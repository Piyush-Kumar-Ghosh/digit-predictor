# 🧠 MNIST Digit Recognizer - Streamlit App

This is a simple and interactive web app that recognizes handwritten digits using a Convolutional Neural Network (CNN) trained on the MNIST dataset. Built with [Streamlit](https://streamlit.io), this app lets users draw digits directly in the browser and get real-time predictions.

---

## 🚀 Live Demo

🔗 [Try the app on Streamlit](https://digit-predictor-hqfeqrpxxs5vvkgefv7ltp.streamlit.app/)


---

## 🖼️ App Features

- Draw a digit (0-9) in the canvas
- Live prediction with confidence scores
- Built using TensorFlow + Streamlit

---

## 🧠 Model Info

- Trained on the MNIST dataset
- 2 Convolutional layers + Dense layers
- Accuracy: ~98% on test set
- Saved as: `mnist_digit_model.keras`

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/Piyush-Kumar-Ghosh/digit-predictor.git
cd digit-predictor
pip install -r requirements.txt
streamlit run app.py
