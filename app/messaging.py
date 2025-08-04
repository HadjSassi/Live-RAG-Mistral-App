import streamlit as st

def send_and_clear():
    message = st.session_state.input_message.strip()
    if message:
        st.session_state.chat_history.append({"sender": "user", "message": message})
        st.session_state.chat_history.append({"sender": "bot", "message": message})
    st.session_state.input_message = ""