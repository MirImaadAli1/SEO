import os
import ai21
import streamlit as st
from dotenv import load_dotenv
import time

# Load secrets
load_dotenv()

# def start_time():
#     starting_time = time.time()
#     return starting_time

st.title("Keyword Generator")
st.write("Enter your business name to generate related keywords for search engine optimization.")

business_name = st.text_input("Enter your business name here")

# dashboard features
st.slider('Pick no. of words', 5, 30)
creativity_value = st.slider('Creativity level', 0.0, 1.0, 0.6, step=0.1)

def generate_keywords():
     st.write("coffee shop, Dubai, United Arab Emirates, Emirati coffee, Arabic coffee, tea, cappuccino, mocha, espresso, latte, barista, coffeehouse, specialty coffee, hummus, shawarma, coffee beans, roasted coffee, coffee grinder, coffee cup")

if st.button("Generate Keywords"):
    st.subheader("Keywords:")
    generate_keywords()



# start_time = time.time()
# end_time = time.time()
#st.write("Time taken to generate: ", end_time - start_time())
