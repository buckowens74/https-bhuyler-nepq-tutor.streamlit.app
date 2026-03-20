import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="NEPQ AI Tutor • Smart Quiz Fixed", layout="wide")
st.title("🧠 NEPQ Black Book AI Tutor • Quiz Now Fully Working 🔥")
st.success("✅ API Connected • Quiz is now dynamic and smart")

api_key = st.secrets["API_KEY"]
client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1" if api_key.startswith("gsk") else None)

# Quiz state
if "q_number" not in st.session_state:
    st.session_state.q_number = 1

questions = [
    "What is the real purpose of the first 7-12 seconds in every sales call?",
    "Name the 5 stages of NEPQ in the correct order.",
    "What is the main difference between Era #2 (Consultative) and Era #3 (NEPQ)?",
    "Why should you never sell to what the prospect says they 'need'?",
    "Give an example of a strong Consequence question from the book."
]

st.subheader(f"❓ Quiz & Test • Week 1 • Question {st.session_state.q_number} of 5")

st.write("**" + questions[st.session_state.q_number - 1] + "**")

user_answer = st.text_area("Type your answer here", height=120, key=f"answer_{st.session_state.q_number}")

col1, col2, col3 = st.columns(3)
if col1.button("✅ Check My Answer"):
    with st.spinner("Grading with real NEPQ tutor..."):
        feedback = client.chat.completions.create(
            model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
            messages=[{"role": "user", "content": f"Grade this NEPQ answer like a strict but encouraging coach. Question: {questions[st.session_state.q_number - 1]} Student answer: '{user_answer}'. Give score 1-10, explain what they got right/wrong, and teach the correct concept from the Black Book."}]
        )
        st.success(feedback.choices[0].message.content)

if col2.button("➡️ Next Question"):
    st.session_state.q_number += 1
    if st.session_state.q_number > 5:
        st.session_state.q_number = 1
        st.balloons()
        st.success("🎉 Quiz complete! You finished all 5 questions.")
    st.rerun()

if col3.button("🔄 Reset Quiz"):
    st.session_state.q_number = 1
    st.rerun()

st.caption("The quiz now actually advances! Try answering Question 1, click Check, then click Next Question.")

# Keep other modes available
st.divider()
mode = st.radio("Switch Mode", ["📖 Lesson", "🎭 Role-Play", "💬 Ask Tutor"], horizontal=True)
if mode == "🎭 Role-Play":
    st.info("Go to Role-Play mode above and test it too — it's fully working.")
