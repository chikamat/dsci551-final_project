import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Set layout to wide
st.set_page_config(layout="wide")

with st.container():
    st.write("Welcome to the Exchange Market!")
st.markdown("<hr style='margin-top: -10px;'>", unsafe_allow_html=True)


# Add your logo image file
logo = Image.open("logo2.png")

image_below_title = Image.open("lfx.jpg")

# Define the layout proportions
col1_width = 1
col2_width = 11

# Display the logo on the left side
col1, col2 = st.columns([col1_width, col2_width])
with col1:
    st.image(logo, width=100)

# Title on the right side
with col2:
    st.markdown("<h1 style='margin-top: -10px;'>Local Food Exchange Network</h1>", unsafe_allow_html=True)
    #st.image(image_below_title, width=600)

st.markdown("<hr style='margin-top: 0px;'>", unsafe_allow_html=True)

# Horizontal menu bar with buttons
menu_options = ["Home", "Products", "Contact Us"]
col1, col2, col3 = st.columns(3)
st.markdown("<hr style='margin-top: 0px;'>", unsafe_allow_html=True)


if col1.button("Home"):
    # Display radio buttons for "Farmer" and "User" within the "Home" section
    with st.container():
        # st.write("Welcome to the Home Page!")
        st.image(image_below_title, width=1230)
        user_type = st.radio("Select User Type", ["Farmer", "User"])
        if user_type == "Farmer":
            # Function for Farmer
            st.write("This is the Farmer section.")
            # Add your farmer-related functionality here
        elif user_type == "User":
            # Function for User
            st.write("This is the User section.")

if col2.button("Products"):
    st.write("Here are our products.")
    # Create expanders for categories
    with st.expander("Vegetables"):
            st.write("Here are our fresh vegetables.")
            # Add your vegetable products here
            vegetables_list = ["Tomato", "Potato", "Onion"]
            for vegetable in vegetables_list:
                if st.button(vegetable):
                    # Display product details when vegetable is clicked
                    if vegetable == "Tomato":
                        st.write("Tomato details: Description, Price, etc.")
                    elif vegetable == "Potato":
                        st.write("Potato details: Description, Price, etc.")
                    elif vegetable == "Onion":
                        st.write("Onion details: Description, Price, etc.")
    with st.expander("Fruits"):
            st.write("Here are our fresh fruits.")
            # Add your fruit products here
    with st.expander("Frozen"):
        st.write("Here are our frozen products.")
        # Add your frozen products here
    with st.expander("Canned"):
        st.write("Here are our canned products.")
        # Add your canned products here

if col3.button("Contact Us"):
    st.write("Our Location")
    st.write("Address: 123 Maple Street")
    st.write("Phone Number: +123 456 7890")
    st.markdown("<hr style='margin-top: 0px;'>", unsafe_allow_html=True)
    st.write("Contact Us")
    contact_form = """
    <form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Name" required>
         <input type="email" name="email" placeholder="Email" required>
         <input type="email" name="email" placeholder="Phone No." required>
         <textarea name="message" placeholder="Enquiry"></textarea>
         <div style="text-align: left;">
            <button type="submit">Send</button>
         </div>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")