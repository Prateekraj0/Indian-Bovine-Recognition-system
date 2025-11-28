# pages/3_Dataset_Info.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset Info", layout="centered")
st.title("📁 Dataset Information")

import streamlit as st

st.markdown("""
<style>
.stApp {
    background-image: url("https://t4.ftcdn.net/jpg/07/84/61/97/360_F_784619757_esWa0aZ5z82Etm3YCaA8CiaOKbaXvdFD.jpg");
    background-size: cover;
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)

st.markdown("### Class counts (from your earlier summary)")

data = {
    "Class": [
        "Ayrshire","Dangi","Kangayam","Amritmahal","Kenkatha","Jaffrabadi",
        "Guernsey","Kasargod","Deoni","Holstein_Friesian","Gir","Brown_Swiss",
        "Alambadi","Kankrej","Bhadawari","Banni","Jersey","Bargur","Hariana","Hallikar"
    ],
    "Images": [
        234,79,90,92,50,101,119,90,96,328,357,225,99,174,86,105,203,90,126,185
    ]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.markdown("### Distribution chart")
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,4))
ax.bar(df["Class"], df["Images"])
ax.set_xticklabels(df["Class"], rotation=45, ha="right")
ax.set_ylabel("Number of images")
plt.tight_layout()
st.pyplot(fig)
