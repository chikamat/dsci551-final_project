import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import uuid

# Set layout to wide
st.set_page_config(layout="wide")

with st.container():
    st.write("Welcome to the Exchange Market!")
st.markdown("<hr style='margin-top: -10px;'>", unsafe_allow_html=True)


# Add your logo image file
logo = Image.open("logo.png")

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
selected = option_menu(
    menu_title=None,  # required
    options=["Home", "Products", "Contact Us"],  # required
    icons=["house", "basket2-fill", "envelope"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
        )
st.markdown("<hr style='margin-top: 0px;'>", unsafe_allow_html=True)
def generate_sample_product_list():
    sample_data = [
        {"category": "Vegetables", "name": "Tomato", "inventory": 100, "price": 1.5},
        {"category": "Vegetables", "name": "Potato", "inventory": 80, "price": 2.0},
        {"category": "Fruits", "name": "Apple", "inventory": 120, "price": 1.0},
        {"category": "Fruits", "name": "Banana", "inventory": 150, "price": 0.5},
        {"category": "Frozen", "name": "Orange", "inventory": 200, "price": 2.5},
        {"category": "Frozen", "name": "Mango", "inventory": 90, "price": 3.0},
        {"category": "Canned", "name": "Peaches", "inventory": 60, "price": 2.0},
        {"category": "Canned", "name": "Mandarins", "inventory": 75, "price": 1.8},
    ]
    return sample_data

def generate_sample_product_list1():
    products = [
        {"id": 1, "category": "Vegetables", "name": "Tomato", "price": 0.99, "review": 4},
        {"id": 2, "category": "Vegetables", "name": "Potato", "price": 0.50, "review": 4},
        {"id": 3, "category": "Fruits", "name": "Apple", "price": 1.20, "review": 4},
        {"id": 4, "category": "Fruits", "name": "Banana", "price": 0.60, "review": 4},
    # Add more products as needed
    ]
    return products


def display_product_details():
    # Assuming you have product details in a dictionary or similar structure
    product_details = {
        "Name": "Example Product",
        "Price": "$10",
        "Description": "This is an example product description."
    }

    st.title("Checkout")
    for key, value in product_details.items():
        st.write(f"{key}: {value}")

if selected == "Home":
    # Display radio buttons for "Farmer" and "User" within the "Home" section
    with st.container():
        st.image(image_below_title, width=1230)
        user_type = st.radio("Select User Type", ["Farmer", "User"])
        st.markdown("<hr style='margin-top: 10px;'>", unsafe_allow_html=True)

        if user_type == "Farmer":
            # This is the Farmer section
            st.write("This is the Farmer section.")

            # Buttons for different options
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("Sign Up"):
                    st.session_state['farmer_action'] = 'sign_up'
            with col2:
                if st.button("Add Products"):
                    st.session_state['farmer_action'] = 'add_products'
            with col3:
                if st.button("Product List (Update/Delete)"):
                    st.session_state['farmer_action'] = 'product_list'

            # Check session state to display the correct form or list
            if 'farmer_action' in st.session_state:
                if st.session_state['farmer_action'] == 'sign_up':
                    with st.form("Farmer_Sign_Up", clear_on_submit=True):
                        # Create columns for a tighter layout. Adjust the number in 'columns' for desired width.
                        col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratio as needed

                        with col2:  # Use the middle column for inputs
                            name = st.text_input("Name")
                            phone_number = st.text_input("Phone Number")
                            location = st.text_input("Location")

                        with col2:  # Place the submit button in the middle column
                            submit_button = st.form_submit_button("Submit")

                        if submit_button:
                            # Generate a unique user ID for the farmer
                            user_id = str(uuid.uuid4())
                            # Display the success message along with the user ID
                            st.success(f"Sign up successful for {name}. Your ID is: {user_id}")
                elif st.session_state['farmer_action'] == 'add_products':
                    with st.form("Add_Products", clear_on_submit=True):
                        col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratio as needed

                        with col2:
                            your_ID = st.text_input("Your ID")
                            main_category = st.selectbox("Select Main Category",
                                                     ["Vegetables", "Fruits", "Frozen", "Canned"])

                        # Subcategory dropdown based on the main category selection
                            #if main_category == "Vegetables":
                                #subcategories = ["Tomato", "Potato", "Onion", "Carrot"]
                            #elif main_category == "Fruits":
                                #subcategories = ["Apple", "Banana", "Orange", "Blueberry"]
                            #elif main_category == "Frozen":
                                #subcategories = ["Orange", "Blueberry", "Mango"]
                            #elif main_category == "Canned":
                                #subcategories = ["Grapefruit", "Peaches", "Mandarins"]
                            #else:
                                #subcategories = ["Miscellaneous"]
                            sub_category = st.text_input("Product Name")
                            price = st.number_input("Price per unit", min_value=0.0)
                            quantity = st.number_input("Inventory", min_value=0)
                            add_button = st.form_submit_button("Add Product")
                            if add_button:
                                st.success(f"Product {your_ID} added successfully.")
                            # Handle saving or processing product details
                elif st.session_state['farmer_action'] == 'product_list':
                    with st.form("product_list", clear_on_submit=True):
                        col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratio as needed
                        with col2:  # Use the middle column for inputs
                            your_ID = st.text_input("Your ID")
                            submit_button = st.form_submit_button("Submit")
                        if submit_button:
                            product_list = generate_sample_product_list()
                            col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratio as needed
                            with col2:
                                st.write("Product List:")
                                if product_list:
                                # Define the table headers
                                    st.write("| Category | Product | Inventory | Price | Update | Delete |")
                                # Display each product in a row
                                    for product in product_list:
                                        category = product['category']
                                        name = product['name']
                                        inventory = product['inventory']
                                        price = product['price']
                                        st.write(
                                        f"| {category} | {name} | {inventory} | {price} | [Update](#) | [Delete](#) |")
                                else:
                                    st.write("No products found.")


        elif user_type == "User":

            st.write("This is the User section.")

            with st.form("Home", clear_on_submit=True):

                col1, col2, col3 = st.columns([1, 2, 1])

                with col2:

                    main_category = st.selectbox("Select Main Category",

                                                 ["Vegetables", "Fruits", "Frozen", "Canned"])

                    sub_category = st.text_input("Product Name")

                    add_button = st.form_submit_button("Search")

                    if add_button:

                        product_list = generate_sample_product_list1()

                        st.write("Product List:")

                        if product_list:

                            # Define the table headers

                            st.write("| Category | Product | Price | Review | Buy |")

                            # Display each product in a row

                            for product in product_list:
                                category = product['category']

                                name = product['name']

                                price = product['price']

                                review = product['review']

                                st.write(

                                    f"| {category} | {name} | {price} | {review} | [Buy](#) |")

                        else:

                            st.write("No products found.")

            if add_button:  # Checking if the search button is clicked

                with st.form("Checkout", clear_on_submit=True):
                    st.header("Your Shopping Cart")

                    st.write("| Category | Product | Price | Review | Buy |")

                    # Add items to cart here

if selected == "Products":
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
            fruits_list = ["Orange", "Apple", "Blueberry"]
            for fruit in fruits_list:
                if st.button(fruit):
                    # Display product details when vegetable is clicked
                    if fruit == "Orange":
                        st.write("Orange details: Description, Price, etc.")
                    elif fruit == "Apple":
                        st.write("Apple details: Description, Price, etc.")
                    elif fruit == "Blueberry":
                        st.write("Blueberry details: Description, Price, etc.")
    with st.expander("Frozen"):
        st.write("Here are our frozen products.")
        # Add your frozen products here
        frozen_list = ["orange", "blueberry", "mango"]
        for frozen in frozen_list:
            if st.button(frozen):
                # Display product details when vegetable is clicked
                if frozen == "orange":
                    st.write("Orange details: Description, Price, etc.")
                elif frozen == "blueberry":
                    st.write("Blueberry details: Description, Price, etc.")
                elif frozen == "mango":
                    st.write("Mango details: Description, Price, etc.")
    with st.expander("Canned"):
        st.write("Here are our canned products.")
        # Add your canned products here
        canned_list = ["Grapefruit", "Peaches", "Mandarins"]
        for canned in canned_list:
            if st.button(canned):
                # Display product details when vegetable is clicked
                if canned == "Grapefruit":
                    st.write("Grapefruit details: Description, Price, etc.")
                elif canned == "Peaches":
                    st.write("Peaches details: Description, Price, etc.")
                elif canned == "Mandarins":
                    st.write("Mandarins details: Description, Price, etc.")

if selected == "Contact Us":
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
         <input type="text" name="email" placeholder="Phone No." required>
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