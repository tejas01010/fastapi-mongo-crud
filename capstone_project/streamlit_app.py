import streamlit as st
import requests
import uuid
from app.core.config import BACKEND_API_URL

API_URL = BACKEND_API_URL


st.set_page_config(
    page_title="History & Philosophy Tutor",
    page_icon="📜",
    layout="centered"
)

st.title("📜 History & Philosophy Tutor")
st.caption("A calm academic tutor that explains step by step")

# -----------------------------
# SESSION STATE
# -----------------------------
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# RESET BUTTON
# -----------------------------
if st.button("🔄 New Conversation"):
    st.session_state.conversation_id = str(uuid.uuid4())
    st.session_state.messages = []
    st.rerun()

# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)

# -----------------------------
# USER INPUT
# -----------------------------
user_input = st.chat_input("Ask about history or philosophy...")

if user_input:
    # Show user message immediately
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    payload = {
        "question": user_input,
        "conversation_id": st.session_state.conversation_id
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()

        tutor_reply = data["answer"]

    except Exception as e:
        tutor_reply = "⚠️ Sorry, something went wrong while contacting the tutor."

    # Show tutor reply
    st.session_state.messages.append(("assistant", tutor_reply))
    with st.chat_message("assistant"):
        st.markdown(tutor_reply)
