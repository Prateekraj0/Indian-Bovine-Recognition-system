# app.py
import streamlit as st
import requests
import os
import gdown
from ultralytics import YOLO
from PIL import Image

# -----------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------
st.set_page_config(
    page_title="Indian Bovine App",
    layout="wide",
    page_icon="🐄"
)

# -----------------------------------------------------------
# LOAD MODEL (FROM GOOGLE DRIVE)
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
# STYLING + BACKGROUND
# -----------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/premium-photo/playfully-quirky-cow-stylish-glasses-against-bright-background_1228868-21391.jpg?semt=ais_hybrid&w=740&q=80");
        background-size: cover;
        background-attachment: fixed;
    }

    .overlay {
        background: rgba(255, 255, 255, 0.80);
        padding: 30px;
        border-radius: 18px;
        backdrop-filter: blur(4px);
    }

    .banner {
        background: linear-gradient(90deg, #0f172a, #1e293b);
        padding: 40px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.25);
    }

    .card {
        background: rgba(255, 255, 255, 0.92);
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }

    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
# LOAD LOTTIE ANIMATION
# -----------------------------------------------------------
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

LOTTIE_COW_URL = "https://assets4.lottiefiles.com/packages/lf20_2glqweqs.json"

# -----------------------------------------------------------
# HEADER
# -----------------------------------------------------------
st.markdown("<div class='banner'>", unsafe_allow_html=True)
st.markdown(
    """
    <h1>🐄 Indian Bovine Breed Recognition</h1>
    <h3>AI-Powered Identification of Indian Cattle & Buffalo Breeds</h3>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------
# COW ANIMATION
# -----------------------------------------------------------
st.components.v1.html(
    f"""
    <div style="display:flex; justify-content:center;">
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player 
            src="{LOTTIE_COW_URL}"
            background="transparent"
            speed="1"
            style="width: 350px; height: 350px;"
            loop
            autoplay>
        </lottie-player>
    </div>
    """,
    height=350,
)

# -----------------------------------------------------------
# MAIN CONTENT
# -----------------------------------------------------------
st.markdown("<div class='overlay'>", unsafe_allow_html=True)

# Project Overview
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>📌 Project Overview</div>", unsafe_allow_html=True)
st.write("""
This application uses a **YOLOv8 Classification Model** to identify Indian cattle & buffalo breeds.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Supported Breeds
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>🐃 Supported Breeds</div>", unsafe_allow_html=True)

if CLASS_NAMES:
    st.write(f"**Total Breeds:** {len(CLASS_NAMES)}")
    st.write(CLASS_NAMES)
else:
    st.error("class_names.txt not found!")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------
# IMAGE UPLOAD + PREDICTION
# -----------------------------------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>📤 Upload Image for Prediction</div>", unsafe_allow_html=True)

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

    st.success(f"🐄 Predicted Breed: **{breed}**")
    st.info(f"Confidence: {confidence:.2f}")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.info(f"Loaded {len(CLASS_NAMES)} breeds")
