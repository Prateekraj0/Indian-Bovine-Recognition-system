# pages/2_Training_Results.py
import streamlit as st
import os
from PIL import Image
import pandas as pd


st.set_page_config(page_title="Training Results", layout="centered")
st.title("📊 Training Results & Metrics")

import streamlit as st

st.markdown("""
<style>
.stApp {
    background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20230714/pngtree-playful-3d-illustration-of-a-cow-image_3879186.jpg");
    background-size: cover;
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)

assets_dir = "assets"
confusion_path = os.path.join(assets_dir, "confusion_matrix.png")
results_plot = os.path.join(assets_dir, "results.png")
csv_path = os.path.join(assets_dir, "results.csv")

st.markdown("### Visualizations")

if os.path.exists(results_plot):
    st.image(results_plot, caption="Training results (loss/accuracy)", use_column_width=True)
else:
    st.info("No `results.png` found in assets/ — optional but helpful.")

if os.path.exists(confusion_path):
    st.image(confusion_path, caption="Confusion Matrix", use_column_width=True)
else:
    st.info("No `confusion_matrix.png` found in assets/.")

st.markdown("---")
st.markdown("### Additional files (optional)")
if os.path.exists(csv_path):
    try:
        df = pd.read_csv(csv_path)
        st.dataframe(df)
    except Exception as e:
        st.write("Couldn't load results.csv:", e)
else:
    st.info("No `results.csv` found in assets/")
