# pages/1_Prediction.py
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Prediction", layout="centered")

# Paths
MODEL_PATH = "models/bovine_best.pt"
CLASS_NAMES_PATH = "class_names.txt"

import streamlit as st

st.markdown("""
<style>
.stApp {
    background-image: url("");
    background-size: cover;
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)
# Load class names
if not os.path.exists(CLASS_NAMES_PATH):
    st.error(f"Missing {CLASS_NAMES_PATH}. Create it with one class per line.")
    st.stop()

with open(CLASS_NAMES_PATH, "r") as f:
    CLASS_NAMES = [l.strip() for l in f.readlines() if l.strip()]
NUM_CLASSES = len(CLASS_NAMES)

# Load model cached
@st.cache_resource
def load_model(path):
    if not os.path.exists(path):
        return None, f"Model not found at {path}."
    model = YOLO(path)
    return model, None

model, err = load_model(MODEL_PATH)
if err:
    st.error(err)
    st.stop()

st.title("📸 Predict Bovine Breed")
st.write("Upload a clear image of the animal (jpg/png). Frontal or side images work best.")

uploaded = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])
if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Uploaded image", use_column_width=True)

    with st.spinner("Running inference..."):
        arr = np.array(img)
        results = model(arr, verbose=False)
    r = results[0]

    if not hasattr(r, "probs"):
        st.error("Model output doesn't contain `probs`. Make sure the model is a YOLOv8 classification model.")
        st.stop()

    # Extract probabilities
    try:
        top1_idx = int(r.probs.top1)
        top1_conf = float(r.probs.top1conf)
        top5_idxs = [int(x) for x in r.probs.top5]
        top5_confs = [float(x) for x in r.probs.top5conf]
        all_probs = r.probs.data.cpu().numpy().ravel()
    except Exception as e:
        st.error(f"Failed to parse model output: {e}")
        st.stop()

    # Map indices -> names (use your class list)
    def idx2name(i):
        return CLASS_NAMES[i] if 0 <= i < NUM_CLASSES else f"Class_{i}"

    pred_name = idx2name(top1_idx)
    st.success(f"### 🐄 Predicted: **{pred_name}**")
    st.info(f"Confidence: **{top1_conf*100:.2f}%**")

    # Confidence meter
    st.markdown("#### Confidence meter")
    st.progress(int(top1_conf*100))

    # Top-5 horizontal bar chart
    st.markdown("#### Top-5 predictions")
    top5_labels = [idx2name(i) for i in top5_idxs]
    top5_vals = [v*100 for v in top5_confs]

    fig, ax = plt.subplots(figsize=(7, 3))
    y = np.arange(len(top5_labels))
    ax.barh(y, top5_vals[::-1], height=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels([l for l in top5_labels[::-1]])
    ax.set_xlabel("Confidence (%)")
    ax.set_xlim(0, 100)
    for i, v in enumerate(top5_vals[::-1]):
        ax.text(v + 1, i, f"{v:.2f}%", va="center")
    plt.tight_layout()
    st.pyplot(fig)

    # Pie chart of top-N probabilities
    st.markdown("#### Probability distribution (Top 8 shown)")
    topN = min(8, len(all_probs))
    topN_idx = np.argsort(all_probs)[-topN:][::-1]
    pie_labels = [idx2name(i) for i in topN_idx]
    pie_vals = all_probs[topN_idx]

    fig2, ax2 = plt.subplots(figsize=(5,5))
    ax2.pie(pie_vals, labels=pie_labels, autopct="%1.1f%%", startangle=140)
    ax2.axis("equal")
    st.pyplot(fig2)

else:
    st.info("Upload an image to get a prediction.")
