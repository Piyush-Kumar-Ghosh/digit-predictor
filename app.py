
import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from streamlit_drawable_canvas import st_canvas

model = tf.keras.models.load_model("mnist_digit_model.h5")

st.title("🧠 MNIST Digit Recognizer")
st.write("Draw a digit (0-9) and the model will predict it!")

canvas_result = st_canvas(
    fill_color="#000000",
    stroke_width=10,
    stroke_color="#FFFFFF",
    background_color="#000000",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    img = canvas_result.image_data[:, :, 0]  # Get 1 channel (grayscale)
    img = Image.fromarray(img).resize((28, 28)).convert("L")
    img = np.array(img)
    img = img.reshape(1, 28, 28, 1) / 255.0

    # Check if the drawing is basically blank
    if np.sum(img) < 10:
        st.warning("🖼️ Please draw a digit before predicting.")
    else:
        pred = model.predict(img)
        predicted_digit = np.argmax(pred)
        st.subheader(f"Predicted Digit: {predicted_digit}")
