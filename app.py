import streamlit as st
from questions import questions

st.title("🎵 Moodify")
st.subheader("Discover Your Music Personality")

scores = {
    "Happy": 0,
    "Sad": 0,
    "Energetic": 0,
    "Calm": 0
}

answers = []

for question, options in questions.items():
    answer = st.radio(question, list(options.keys()))
    answers.append(options[answer])

if st.button("Analyze Personality"):
    for trait in answers:
        scores[trait] += 1

    personality = max(scores, key=scores.get)

    st.success(f"Your Personality Type: {personality}")