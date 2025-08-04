import streamlit as st

def render_conversation():
    dialogue_placeholder = st.empty()
    with dialogue_placeholder.container():
        st.title("Conversation")
        for entry in st.session_state.chat_history:
            if entry["sender"] == "user":
                col1, col2 = st.columns([1, 5])
                with col2:
                    st.markdown(
                        "<div style='text-align: right; padding: 10px; border-radius: 10px; "
                        "margin-bottom: 5px; margin-right: 5px; max-width: 95%; overflow-wrap: break-word; "
                        "background-color: #AAAAAA; color: black;'>"
                        "<strong>Vous :</strong> " + entry['message'] + "</div>",
                        unsafe_allow_html=True
                    )
            else:
                col1, col2 = st.columns([5, 1])
                with col1:
                    st.markdown(
                        "<div style='text-align: left; padding: 10px; border-radius: 10px; "
                        "margin-bottom: 5px; max-width: 80%; overflow-wrap: break-word; "
                        "background-color: #333333; color: white;'>"
                        "<strong>Bot :</strong> " + entry['message'] + "</div>",
                        unsafe_allow_html=True
                    )