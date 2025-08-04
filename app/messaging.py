import streamlit as st

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.databaseDescription import get_full_database_info
from utils.rag import handle_contextual_query
from utils.sql import handle_relational_query
from utils.sql.relational_detector import is_relational_query

def send_and_clear():
    message = st.session_state.input_message.strip()
    if message:
        st.session_state.chat_history.append({"sender": "user", "message": message})
        if is_relational_query(message, get_full_database_info()):
            answer = handle_relational_query(message, get_full_database_info())
        else:
            answer = handle_contextual_query(message)
        st.session_state.chat_history.append({"sender": "bot", "message": answer})
    st.session_state.input_message = ""