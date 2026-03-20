import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="NEPQ AI Tutor • Fully Fixed", layout="wide")
st.title("🧠 NEPQ Black Book AI Tutor • Fully Working & Easy to Use 🔥")
st.success("✅ Everything fixed • Click the top buttons to switch modes")

api_key = st.secrets["API_KEY"]
client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1" if api_key.startswith("gsk") else None)

# Top Mode Selector
mode = st.radio("Select Mode 👇", 
                ["📖 Guided Lesson", "🎭 Role-Play Simulator", "💬 Ask Tutor Anything", "❓ Quiz & Test"], 
                horizontal=True, label_visibility="visible")

st.divider()

if mode == "📖 Guided Lesson":
    st.subheader("📖 Today's Lesson • Week 1")
    st.write("**Focus:** The first 7-12 seconds + Connection Questions (pages 17-24)")
    if st.button("Give me script + practice drill"):
        with st.spinner("Tutor preparing..."):
            r = client.chat.completions.create(model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": "Give a clear example of a NEPQ Connection script for an inbound lead + 3 practice lines"}])
            st.success(r.choices[0].message.content)

elif mode == "🎭 Role-Play Simulator":
    st.subheader("🎭 Role-Play Simulator")
    scenario = st.selectbox("Choose scenario", ["Inbound Zoom - Life Insurance", "Cold Call - Auto", "Solar Consequence", "Objection: I need to think"])
    your_line = st.text_area("Type what YOU would say:")
    if st.button("🚀 Send my line → AI plays Prospect + Coaches"):
        with st.spinner("Prospect responding..."):
            r = client.chat.completions.create(model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": f"NEPQ role-play. Scenario: {scenario}. Salesperson just said: '{your_line}'. Respond as prospect then coach using Black Book."}])
            st.markdown("**Prospect:** " + r.choices[0].message.content)

elif mode == "💬 Ask Tutor Anything":
    st.subheader("💬 Ask the NEPQ Tutor")
    q = st.chat_input("Example: How do I ask a good Consequence question for HVAC?")
    if q:
        with st.spinner("Tutor answering..."):
            r = client.chat.completions.create(model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": f"Expert NEPQ tutor answer: {q}"}])
            st.success(r.choices[0].message.content)

elif mode == "❓ Quiz & Test":
    st.subheader("❓ Quiz & Test")
    
    # Quiz logic
    if "q_num" not in st.session_state:
        st.session_state.q_num = 1
    
    qs = [
        "What is the purpose of the first 7-12 seconds?",
        "Name the 5 stages of NEPQ in order.",
        "What is the difference between Era #2 and Era #3?",
        "Why do we use verbal pauses (...) ?",
        "Give an example of a strong Problem Awareness question."
    ]
    
    st.write(f"**Question {st.session_state.q_num}/5:** {qs[st.session_state.q_num-1]}")
    ans = st.text_area("Your answer", height=100)
    
    col1, col2 = st.columns(2)
    if col1.button("✅ Check My Answer"):
        with st.spinner("Grading..."):
            fb = client.chat.completions.create(model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": f"Grade this answer strictly but encouragingly. Question: {qs[st.session_state.q_num-1]} Answer: '{ans}'. Score + explanation + correct teaching from Black Book."}])
            st.success(fb.choices[0].message.content)
    
    if col2.button("➡️ Next Question"):
        st.session_state.q_num += 1
        if st.session_state.q_num > 5:
            st.session_state.q_num = 1
            st.balloons()
            st.success("🎉 You completed the full quiz!")
        st.rerun()

st.caption("✅ Modes should now switch instantly. Try clicking each top button.")
st.info("💡 Best test: Switch to Role-Play → type a line → click the send button")
