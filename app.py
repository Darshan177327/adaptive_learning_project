import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.cognitive_state import detect_cognitive_state
from src.adaptive_content import get_adaptive_content

import streamlit as st
from src.cognitive_state import detect_cognitive_state
from src.adaptive_content import get_adaptive_content

st.title("Adaptive Learning System")

pauses = st.number_input("Pauses", min_value=0)
rewinds = st.number_input("Rewinds", min_value=0)
idle_time = st.number_input("Idle Time (seconds)", min_value=0)
tab_switch = st.number_input("Tab Switch Count", min_value=0)
quiz_score = st.number_input("Quiz Score (0–100)", min_value=0, max_value=100)
fast_forward = st.number_input("Fast Forward Count", min_value=0)

if st.button("Analyze"):
    state = detect_cognitive_state(pauses, rewinds, idle_time, tab_switch, quiz_score, fast_forward)
    content = get_adaptive_content(state)

    st.success(f"Cognitive State Detected: {state}")
    st.info(f"Recommended Content: {content}")
