import streamlit as st

from messaging import send_and_clear
from rendering import render_conversation

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

render_conversation()

with st.form("chat_form"):
    st.text_input("Tapez votre message ici", key="input_message")
    submitted = st.form_submit_button("Envoyer", on_click=send_and_clear)