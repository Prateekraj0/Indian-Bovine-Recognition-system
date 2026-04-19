import streamlit as st
import os

# -----------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------
st.set_page_config(
    page_title="Indian Bovine App",
    layout="wide",
    page_icon="🐄"
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
# HEADER
# -----------------------------------------------------------
st.title("🐄 Indian Bovine Breed Recognition System")
st.write("👈 Use the sidebar to navigate between pages")

# -----------------------------------------------------------
# OVERVIEW
# -----------------------------------------------------------
st.subheader("📌 Project Overview")
st.write("""
This project uses a **YOLOv8 classification model** to identify Indian cattle and buffalo breeds from images.

### Features:
- Breed prediction from images  
- Confidence score  
- Training insights  
- Dataset overview  
""")

# -----------------------------------------------------------
# BREEDS
# -----------------------------------------------------------
st.subheader("🐃 Supported Breeds")

if CLASS_NAMES:
    st.write(f"Total Breeds: {len(CLASS_NAMES)}")
    st.write(CLASS_NAMES)
else:
    st.error("class_names.txt not found!")

# -----------------------------------------------------------
# FOOTER
# -----------------------------------------------------------
st.info("Select a page from sidebar → Prediction / Dataset")
