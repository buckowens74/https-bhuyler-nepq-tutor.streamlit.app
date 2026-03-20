import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="NEPQ AI Tutor • Smart & Interactive", layout="wide")
st.title("🧠 NEPQ Black Book AI Tutor • Now Smart & Interactive 🔥")
st.success("✅ Fully working • AI answers in every mode")

api_key = st.secrets["API_KEY"]
client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1" if api_key.startswith("gsk") else None)

with st.sidebar:
    week = st.selectbox("Week", ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8"])
    mode = st.radio("Mode", ["📖 Lesson", "🎭 Role-Play", "💬 Ask Tutor", "❓ Quiz & Test"], horizontal=True)

st.subheader(f"{mode} • {week}")

if mode == "📖 Lesson":
    st.write("**Today:** Connection Stage – First 7-12 seconds (pages 17-24)")
    if st.button("Give me script + practice"):
        with st.spinner("Tutor preparing..."):
            resp = client.chat.completions.create(model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": "Give a clear Connection script example for an inbound lead + 3 practice lines from the NEPQ Black Book"}])
            st.success(resp.choices[0].message.content)

elif mode == "🎭 Role-Play":
    scenario = st.selectbox("Scenario", ["Inbound Life Insurance", "Cold Call Auto", "Solar Consequence", "Objection Drill"])
    your_line = st.text_area("Type what YOU say to the prospect:")
    if st.button("🚀 Send → Let AI play the Prospect + Coach me"):
        with st.spinner("Prospect is responding..."):
            resp = client.chat.completions.create(model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": f"NEPQ Role-play. Scenario: {scenario}. Salesperson said: '{your_line}'. Respond as a real prospect, then coach using Black Book principles."}])
            st.markdown("**Prospect:** " + resp.choices[0].message.content)

elif mode == "💬 Ask Tutor":
    q = st.chat_input("Ask anything (e.g. How do I ask a good Consequence question?)")
    if q:
        with st.spinner("Tutor thinking..."):
            ans = client.chat.completions.create(model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": f"You are expert NEPQ tutor. Answer clearly and reference the book: {q}"}])
            st.success(ans.choices[0].message.content)

elif mode == "❓ Quiz & Test":
    st.write("**Question 1:** What is the real purpose of the first 7-12 seconds in a sales call?")
    user_answer = st.text_area("Type your answer here", height=100, placeholder="Example: To disarm the prospect and make them curious...")
    
    if st.button("✅ Check My Answer"):
        with st.spinner("Grading + teaching..."):
            feedback = client.chat.completions.create(model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": f"Grade this NEPQ quiz answer like a strict but encouraging coach. Question: What is the purpose of the first 7-12 seconds? Student answer: '{user_answer}'. Give score out of 10, explain what they got right, and teach the exact concept from the Black Book."}])
            st.success(feedback.choices[0].message.content)
    
    if st.button("Next Question"):
        st.write("**Question 2:** Name the 5 stages of NEPQ in order.")

st.caption("This version now uses your real API in every single button. The Quiz finally works!")
st.info("💡 Test it: Go to ❓ Quiz, type any answer, click 'Check My Answer' — you should get real feedback now.")
