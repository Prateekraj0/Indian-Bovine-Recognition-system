# app.py
import streamlit as st
import requests
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
# STYLING + BACKGROUND
# -----------------------------------------------------------
st.markdown(
    """
    <style>
    /* Background Image */
    .stApp {
        background-image: url("https://img.freepik.com/premium-photo/playfully-quirky-cow-stylish-glasses-against-bright-background_1228868-21391.jpg?semt=ais_hybrid&w=740&q=80");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Transparent overlay for content */
    .overlay {
        background: rgba(255, 255, 255, 0.80);
        padding: 30px;
        border-radius: 18px;
        backdrop-filter: blur(4px);
    }

    /* Header Banner */
    .banner {
        background: linear-gradient(90deg, #0f172a, #1e293b);
        padding: 40px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.25);
    }

    /* Cards */
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
# LOAD LOTTIE ANIMATION (cow)
# -----------------------------------------------------------
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Moving cow animation (black and white cow walking)
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
# MAIN CONTENT (OVERVIEW SECTIONS)
# -----------------------------------------------------------
st.markdown("<div class='overlay'>", unsafe_allow_html=True)

# ------------------- Project Overview ----------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>📌 Project Overview</div>", unsafe_allow_html=True)
st.write(
    """
    This application uses a **YOLOv8 Classification Model** to automatically identify
    various Indian Cattle and Buffalo breeds using user-uploaded images.
    
    The project aims to support:
    - Field-level livestock workers  
    - Government breed registry systems  
    - Precision dairy management  
    - Automated breed documentation  
    """
)
st.markdown("</div>", unsafe_allow_html=True)

# ------------------- Technology Stack ----------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>⚙️ Technology Stack</div>", unsafe_allow_html=True)
st.write(
    """
    - **YOLOv8 Classification Model**
    - **PyTorch / Ultralytics**
    - **Streamlit UI**
    - **OpenCV + PIL** for image preprocessing
    - **Python 3.10+**
    """
)
st.markdown("</div>", unsafe_allow_html=True)

# ------------------- Input Features ------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>📥 Input Features</div>", unsafe_allow_html=True)
st.write(
    """
    The system takes a **single image** of:
    - Cattle (Bos indicus)  
    - Buffalo (Bubalus bubalis)

    Recommended guidelines:
    - Clear side profile  
    - Good lighting  
    - Single animal in frame  
    """
)
st.markdown("</div>", unsafe_allow_html=True)

# ------------------- Key Features --------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>⭐ Key Features</div>", unsafe_allow_html=True)
st.write(
    """
    - 🔍 **Real-time breed prediction**  
    - 📊 **Confidence score visualization**  
    - 🧭 **Training results + confusion matrix**  
    - 📁 **Dataset statistics overview**  
    - 🖼️ **Image preview before prediction**  
    """
)
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Supported Breeds -------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>🐃 Supported Breeds</div>", unsafe_allow_html=True)

if CLASS_NAMES:
    st.write(f"**Total Breeds:** {len(CLASS_NAMES)}")
    st.write(CLASS_NAMES)
else:
    st.error("class_names.txt not found! Please add it to project root.")

st.markdown("</div>", unsafe_allow_html=True)

# ------------------- Use Cases -----------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>🚜 Use Cases</div>", unsafe_allow_html=True)
st.write(
    """
    - Government livestock registration systems  
    - Breed certification for farmers  
    - Smart dairy farm applications  
    - Field worker mobile apps  
    - Research on indigenous breeds  
    - Veterinary documentation  
    """
)
st.markdown("</div>", unsafe_allow_html=True)

# End overlay
st.markdown("</div>", unsafe_allow_html=True)

# Footer info
st.info(f"Loaded {len(CLASS_NAMES)} breeds from class_names.txt")
