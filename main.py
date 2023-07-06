import os
import ai21
import streamlit as st
from dotenv import load_dotenv

# Load secrets
load_dotenv()

API_KEY = os.getenv("AI21_LABS_API_KEY")

# Set the API key in the authorization header
ai21.api_key = 'CTxVlNQnPWLulXWQFDAa78ong6KeiWcd'

PROMPT = "Enter your business name: "

# Initialization
if "output" not in st.session_state:
    st.session_state["output"] = ""

def generate_keywords(business_name):
    if not business_name:
        return

    prompt = PROMPT + business_name

    response = ai21.Completion.execute(
        model="j2-jumbo",
        custom_model="seoFinal",
        prompt=prompt,
        max_tokens=300,
        temperature=0.6,
        n=10,
        stop=None,
        log_level=None
    )

    st.session_state["output"] = response.completions[0].data.text
    st.balloons()

st.title("Keyword Generator")
st.write("Enter your business name to generate related keywords for search engine optimization.")

business_name = st.text_input("Enter your business name here")
st.button("Generate Keywords", on_click=lambda: generate_keywords(business_name))
st.write("Keywords:")
st.write(st.session_state["output"])
