# streamlit_app.py

import streamlit as st
import pyshorteners

# Set the title of the Streamlit app
st.title("URL Shortener")

# Input field for the URL
url = st.text_input("Enter the URL you want to shorten:")

# Button to trigger URL shortening
if st.button("Shorten URL"):
    if url:
        try:
            # Create a shortener object using pyshorteners
            s = pyshorteners.Shortener()

            # Shorten the input URL
            shortened_url = s.tinyurl.short(url)

            # Display the shortened URL
            st.success(f"Shortened URL: {shortened_url}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter a valid URL.")

