# app.py
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

st.title("🧠 AI Sentiment Analyzer")
st.write("Enter a sentence or paragraph, and let AI tell the sentiment.")

user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            st.success("✅ Sentiment: Positive 😊")
        elif sentiment < 0:
            st.error("❌ Sentiment: Negative 😠")
        else:
            st.info("ℹ️ Sentiment: Neutral 😐")
