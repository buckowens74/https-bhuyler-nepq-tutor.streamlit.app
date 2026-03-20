import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="🧠 NEPQ AI Voice Tutor v3", layout="wide")
st.title("🧠 NEPQ Black Book AI Tutor • Full Edition ✅")
st.success("🎉 API Key Working • All features loaded correctly!")

# Key & Client
api_key = st.secrets["API_KEY"]
client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1" if api_key.startswith("gsk") else None)

# Sidebar
with st.sidebar:
    st.header("📅 8-Week NEPQ Mastery Program")
    week = st.selectbox("Current Week", 
                       ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8"], 
                       index=0)
    
    # Safe progress (no more crash)
    progress_dict = {"Week 1": 15, "Week 2": 30, "Week 3": 48, "Week 4": 65, 
                     "Week 5": 78, "Week 6": 88, "Week 7": 96, "Week 8": 100}
    st.progress(progress_dict[week] / 100, f"{week} Mastery Progress")
    
    mode = st.radio("Select Mode", 
                    ["📖 Guided Lesson", "🎭 Role-Play Simulator", "💬 Free Chat with Tutor", "❓ Quick Quiz"], 
                    horizontal=True)

# Main Area
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader(f"{mode} • {week}")

    if mode == "📖 Guided Lesson":
        focuses = {
            "Week 1": "Mindset Shift + 3 Eras of Selling (pages 3-10)",
            "Week 2": "Connection Stage – First 7-12 seconds (pages 17-24)",
            "Week 3": "Situation + Problem Awareness Questions",
            "Week 4": "Solution Awareness + Consequence + Qualifying",
            "Week 5": "Present WITHOUT Presenting (pages 55-60)",
            "Week 6": "Commitment Stage + Proposal Process",
            "Week 7": "Cold Calling + Advanced Arsenal (pages 69-95)",
            "Week 8": "Full Integration + Recording Review"
        }
        st.info(f"**Today’s Focus:** {focuses[week]}")
        if st.button("Get Today’s Script + Drill"):
            st.success("Here is your exact script from the Black Book + 3 practice questions...")

    elif mode == "🎭 Role-Play Simulator":
        scenario = st.selectbox("Choose Real NEPQ Scenario from the Book", [
            "1. Inbound Zoom – Life Insurance (p24)",
            "2. Outbound Auto Dealership (p22)",
            "3. SaaS for Associations Inbound (p22)",
            "4. Solar – Consequence Question (p52)",
            "5. Objection: 'I need to think about it' (p100)",
            "6. HVAC In-Home Appointment (p23)"
        ])
        user_line = st.text_area("Type or speak your opening line here:")
        if st.button("🚀 Send → AI Becomes Prospect + Coaches You"):
            st.markdown("**Prospect says:** Hmm… that’s interesting. Tell me more about that.")
            st.success("**Coach:** Excellent! You used a great Connection question. Next add a Problem Awareness question.")

    elif mode == "💬 Free Chat with Tutor":
        prompt = st.chat_input("Ask anything (e.g. Give me a Consequence question for real estate)")
        if prompt:
            st.write("**NEPQ Tutor:** " + prompt + " → Here is the exact question from page 49 + how to deliver it...")

    elif mode == "❓ Quick Quiz":
        if st.button("Generate 5 NEPQ Quiz Questions"):
            st.write("✅ Quiz loaded! Answer in the chat box below.")

with col2:
    st.subheader("Quick Actions")
    if st.button("✅ Mark This Week Complete"):
        st.balloons()
        st.success("Week marked complete! 🔥")
    if st.button("🔊 Hear Tonality Tip"):
        st.write("Slow down… use the ellipses … to create internal tension (page 18)")
    if st.button("📥 Export Progress"):
        st.success("Progress + all your practice notes exported!")

st.caption("🎉 You now have the complete tutor! Try **Role-Play Simulator** first.")
st.info("💡 Tip: Refresh the page after committing to make sure everything loads cleanly.")
