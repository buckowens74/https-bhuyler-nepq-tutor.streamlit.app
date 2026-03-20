import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="NEPQ AI Tutor • Rich Prospect Background", layout="wide")
st.title("🧠 NEPQ Black Book AI Tutor • Dynamic + Rich Prospect Background 🔥")
st.success("✅ Every scenario now includes detailed prospect background")

api_key = st.secrets["API_KEY"]
client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1" if api_key.startswith("gsk") else None)

mode = st.radio("Mode", ["🎭 Dynamic Role-Play (Best)", "📖 Lesson", "💬 Ask Tutor", "❓ Quiz"], horizontal=True)

if mode == "🎭 Dynamic Role-Play (Best)":
    st.subheader("🎭 Dynamic Role-Play • Fresh Scenario + Full Prospect Background Every Time")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🎲 Generate Completely New Scenario + Background", use_container_width=True):
            st.session_state.clear()
            st.rerun()

    with col2:
        industry = st.selectbox("Choose base industry (or Surprise Me)", 
                               ["Surprise Me", "Life Insurance", "Solar", "Auto Sales", "Real Estate", "HVAC", "SaaS", "Recruiting", "Health Insurance", "Custom"])

    if "scenario" not in st.session_state:
        with st.spinner("Creating brand new prospect with rich background..."):
            prompt = f"""Create a completely fresh, never-repeated NEPQ sales scenario.
Use the Black Book only as source material — do NOT copy any examples directly.
Industry: {industry}

Output format exactly like this:

**Prospect Background:**
- Name & Age:
- Job / Situation:
- Family / Personal life:
- Personality & Communication style:
- Current pain / trigger that made them talk to you:
- What they are secretly hoping for:
- Likely objections they will give:
- Current NEPQ stage they are in:

Then say: "Ready when you are. Type your first line as the salesperson." """

            r = client.chat.completions.create(
                model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            st.session_state.scenario = r.choices[0].message.content
            st.session_state.conversation = []

    # Display rich background
    st.info(st.session_state.scenario)

    st.write("**Your turn** — Type your opening line as the salesperson")

    user_line = st.text_area("What do you say?", height=90, placeholder="Hi Michael, it looks like you wanted help with...")

    if st.button("🚀 Send my line → Get realistic reply + Coaching"):
        with st.spinner("Prospect is replying + Coach is analyzing..."):
            prompt = f"""Current scenario + prospect background: {st.session_state.scenario}

Salesperson said: "{user_line}"

Respond in this exact format:

**Prospect:** [Natural, realistic reply — use emotion, hesitation, questions, or light pushback]

**NEPQ Coach Feedback:** 
- Which stage are they in?
- What you did well
- What to improve
- Exact next best question you should ask (make it dynamic and strong)"""

            reply = client.chat.completions.create(
                model="grok-3-mini" if api_key.startswith("gsk") else "gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            ).choices[0].message.content

            st.markdown(reply)

            if "conversation" in st.session_state:
                st.session_state.conversation.append({"user": user_line, "ai": reply})

    if st.button("🔄 New Prospect + New Background"):
        st.session_state.clear()
        st.rerun()

    st.caption("Every new scenario now gives you rich, detailed background on the prospect before you speak.")

else:
    st.write("Switch to Dynamic Role-Play to test the new rich background feature.")

st.info("💡 Best way to use: Click the big 'Generate Completely New Scenario + Background' button → read the detailed prospect info → then start talking.")
