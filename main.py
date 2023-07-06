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
        custom_model = "seoS",
        prompt=prompt,
        maxTokens= token_value,
        temperature=creativity_value,
        topP = 1,
        n=1,
        stop=None,
        log_level=None
    )

    keywords = response.completions[0].data.text
    keywords = keywords.strip().lstrip(',')
    st.session_state["output"] = keywords
    st.balloons()

st.title("Keyword Generator")
st.write("Enter your business name to generate related keywords for search engine optimization.")

business_name = st.text_input("Enter your business name here")
# dashboard features
token_value = st.slider('Pick no. of tokens', 1, 2047)
creativity_value = st.slider('Creativity level', 0.0, 1.0, 0.6, step=0.1)

st.button("Generate Keywords", on_click=lambda: generate_keywords(business_name))
st.write("Keywords:")
st.write(st.session_state["output"])
