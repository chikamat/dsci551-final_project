import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
logo = Image.open("logo.png")
vege = Image.open("vegepic.jpg")

col1_width = 1
col2_width = 8

col1, col2 = st.columns([col1_width, col2_width])
with col1:
    st.image(logo, width=100)

with col2:
    col2.markdown('''
    # Welcome to the Exchange Market👋
    **👈 Select a page from the sidebar**
    ''')

st.image(vege, width=900)