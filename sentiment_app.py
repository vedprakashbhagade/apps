import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis App 🌟")
st.write("Enter text below, and this app will determine its sentiment!")

# User input
user_input = st.text_area("Enter your text here:", placeholder="Type something...")

if user_input:
    # Perform sentiment analysis
    blob = TextBlob(user_input)
    sentiment_score = blob.sentiment.polarity

    # Classify sentiment
    if sentiment_score > 0:
        sentiment = "Positive 😊"
    elif sentiment_score < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    # Display results
    st.subheader("Sentiment Analysis Result:")
    st.write(f"Sentiment: **{sentiment}**")
    st.write(f"Sentiment Score: **{sentiment_score:.2f}**")
else:
    st.info("Please enter some text to analyze.")

