import streamlit as st
import os
import gdown
from ultralytics import YOLO
from PIL import Image

st.title("📤 Breed Prediction")

# -----------------------------------------------------------
# LOAD MODEL FROM GOOGLE DRIVE
# -----------------------------------------------------------
@st.cache_resource
def load_model():
    file_id = "1mVIgL7ZMO9z9Xsfd0raaD5eMRAAQbhE4"
    url = f"https://drive.google.com/uc?id={file_id}"
    model_path = "model.pt"

    if not os.path.exists(model_path):
        gdown.download(url, model_path, quiet=False)

    return YOLO(model_path)

model = load_model()

# -----------------------------------------------------------
# LOAD CLASS NAMES
# -----------------------------------------------------------
def load_class_names(path="class_names.txt"):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]

CLASS_NAMES = load_class_names()

# -----------------------------------------------------------
# IMAGE UPLOAD
# -----------------------------------------------------------
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Predicting..."):
        results = model(image)

    probs = results[0].probs
    top1 = probs.top1
    confidence = probs.top1conf

    if CLASS_NAMES:
        breed = CLASS_NAMES[top1]
    else:
        breed = f"Class {top1}"

    st.success(f"🐄 Predicted Breed: {breed}")
    st.info(f"Confidence: {confidence:.2f}")
