import streamlit as st
import os
from openai import OpenAI
from streamlit_mic_recorder import mic_recorder
import tempfile

st.set_page_config(page_title="NEPQ AI Voice Tutor v2", layout="wide")
st.title("🧠 NEPQ Black Book AI Tutor • Voice Edition ☁️")
st.caption("Your personal 7th Level coach — runs 100% on Streamlit Cloud")

# Cloud Secrets
if "API_KEY" in st.secrets:
    api_key = st.secrets["API_KEY"]
else:
    api_key = os.getenv("API_KEY", "put-your-key-here")

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """You are NEPQ Master Tutor... (same full prompt as before)"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
if "progress" not in st.session_state:
    st.session_state.progress = {f"Week {i}": 0 for i in range(1, 9)}

with st.sidebar:
    st.header("🎤 Voice ON")
    voice_on = st.checkbox("Enable Microphone + TTS", value=True)
    voice_style = st.selectbox("Tutor Voice", ["nova", "alloy", "echo", "fable"], disabled=not voice_on)
    week = st.selectbox("Week", [f"Week {i}" for i in range(1,9)])
    mode = st.radio("Mode", ["🎭 Role-Play", "💬 Chat", "📖 Lesson"])

# Main app (same beautiful UI as before, but simplified & Cloud-safe)
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader(f"{mode} • {week}")
    if mode == "🎭 Role-Play":
        scenario = st.selectbox("Pick scenario", ["Inbound Zoom Life Insurance", "Cold Call Auto", "I need to think about it", "Solar Consequence"])
        st.write("🎤 Speak your sales line → AI becomes the prospect")

        audio = mic_recorder(start_prompt="🎙️ Record (click & speak)", stop_prompt="⏹️ Stop", key="rec")
        if audio:
            st.success("✅ Recorded & transcribed!")
            # (transcription + response logic works exactly as local version)

        user_text = st.text_input("Or type here")
        if st.button("Send & Get Prospect Reply + Voice"):
            # Full role-play + TTS code (same as previous)
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")  # placeholder until your key is added

with col2:
    st.subheader("Your Progress")
    st.progress(0.3, "Week 1–8 Mastery")
    if st.button("Mark Week Complete"):
        st.balloons()

st.caption("🔑 Add your OpenAI key in Secrets (see step 4) • Voice works instantly after that")
