# app/main.py
import streamlit as st
from app.chat import ChatSession
from app.ui import render_greeting, render_candidate_form, render_chat

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f9fafb;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 8px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Keep session alive
if "session" not in st.session_state:
    st.session_state.session = ChatSession()

session: ChatSession = st.session_state.session

# Greeting
render_greeting()

# Candidate form → Chat
if not session.candidate_info:
    form_done = render_candidate_form(session)
    if form_done:
        st.success("Candidate info collected!")
        render_chat(session)
else:
    render_chat(session)
