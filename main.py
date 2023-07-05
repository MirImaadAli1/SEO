import os

import ai21
import streamlit as st
from dotenv import load_dotenv

# Load secrets
load_dotenv()

API_KEY = os.getenv("AI21_LABS_API_KEY")

ai21.api_key = 'wpWtgvZuIZIVzegERbOlbvjAKC49SLEm'

PROMPT = "Based on the description given, name the sport.\nDescription: {description}\n Sport name: "

# Initialization
if "output" not in st.session_state:
    st.session_state["output"] = "Output:"


def guess_sport(inp):
    if not len(inp):
        return None

    prompt = PROMPT.format(description=inp)

    response = ai21.Completion.execute(
    model="j2-ultra",
    custom_model="seo",
    prompt=prompt,
    numResults=1,
    maxTokens=200,
    temperature=0.7,
    topKReturn=0,
    topP=1,
    countPenalty={
        "scale": 0,
        "applyToNumbers": False,
        "applyToPunctuations": False,
        "applyToStopwords": False,
        "applyToWhitespaces": False,
        "applyToEmojis": False
    },
    frequencyPenalty={
        "scale": 0,
        "applyToNumbers": False,
        "applyToPunctuations": False,
        "applyToStopwords": False,
        "applyToWhitespaces": False,
        "applyToEmojis": False
    },
    presencePenalty={
        "scale": 0,
        "applyToNumbers": False,
        "applyToPunctuations": False,
        "applyToStopwords": False,
        "applyToWhitespaces": False,
        "applyToEmojis": False
    },
    stopSequences=[]
)

    st.session_state["output"] = response.completions[0].data.text
    st.balloons()


st.title("Search Engine Optimization Assistant")

st.write(
    "Type in your business or website description to receive keywords to boost your relevance!!"
)


inp = st.text_area("Enter your request here", height=100)
st.button("Gue" "ss", on_click=guess_sport(inp))
st.write(f"Answer: {st.session_state.output}")
