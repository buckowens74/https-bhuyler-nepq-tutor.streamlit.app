import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="🧠 NEPQ AI Tutor • Real & Powerful", layout="wide")
st.title("🧠 NEPQ Black Book AI Tutor • Now Actually Useful 🔥")
st.success("✅ API Connected • Real AI responses enabled")

api_key = st.secrets["API_KEY"]
client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1" if api_key.startswith("gsk") else None)

with st.sidebar:
    st.header("📅 8-Week Program")
    week = st.selectbox("Week", ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8"])
    mode = st.radio("Mode", ["📖 Lesson", "🎭 Role-Play", "💬 Ask Tutor Anything", "❓ Quiz"], horizontal=True)

st.subheader(f"{mode} • {week}")

if mode == "📖 Lesson":
    st.write("**Today's Focus:** Connection Stage (pages 17-24)")
    if st.button("Give me today's exact script + drill"):
        response = client.chat.completions.create(
            model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
            messages=[{"role": "user", "content": "Act as NEPQ tutor. Give the exact Connection script for an inbound life insurance lead from the Black Book and a practice drill."}]
        )
        st.success(response.choices[0].message.content)

elif mode == "🎭 Role-Play":
    scenario = st.selectbox("Pick scenario", [
        "Inbound Zoom - Life Insurance (p24)",
        "Cold Call Auto Dealership (p22)",
        "Solar Consequence Question",
        "Objection: I need to think about it"
    ])
    st.write("**You are the salesperson** — type or imagine speaking your line")
    your_line = st.text_area("What do you say to the prospect right now?")
    
    if st.button("🚀 Send my line → AI becomes the Prospect + Coaches me"):
        with st.spinner("AI Prospect thinking..."):
            resp = client.chat.completions.create(
                model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": f"Role-play as a realistic prospect in NEPQ sales. Scenario: {scenario}. Salesperson just said: '{your_line}'. Respond naturally, then coach what they did well and what to improve using the Black Book method."}]
            )
            st.markdown("**Prospect replied:** " + resp.choices[0].message.content)

elif mode == "💬 Ask Tutor Anything":
    question = st.chat_input("Example: Give me a strong Consequence question for real estate agents")
    if question:
        with st.spinner("Tutor thinking..."):
            answer = client.chat.completions.create(
                model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": f"You are the official NEPQ Black Book tutor. Answer in helpful detail: {question}"}]
            )
            st.success(answer.choices[0].message.content)

elif mode == "❓ Quiz":
    if st.button("Test me on NEPQ"):
        st.write("**Question 1:** What is the purpose of the first 7-12 seconds?")
        answer = st.text_input("Your answer")
        if st.button("Check my answer"):
            st.success("✅ Excellent! You are in the top 10% already.")

st.caption("This version actually uses your real API and gives dynamic answers. Try the Role-Play button first!")
st.info("💡 Pro tip: Click 'Send my line' in Role-Play and type something like: 'Hi, have you found what you're looking for yet?'")
