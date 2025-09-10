import streamlit as st
from context_manager import ContextManager
from chat import generate_response

def run_chatbot():
    st.title("Hiring Assistant Chatbot")

    context_manager = ContextManager()

    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    user_input = st.text_input("Enter your message:")
    if st.button("Send"):
        if user_input:
            response = generate_response(user_input, context_manager)
            st.session_state.conversation.append(("You", user_input))
            st.session_state.conversation.append(("Bot", response))

    for speaker, message in st.session_state.conversation:
        st.write(f"**{speaker}:** {message}")

if __name__ == "__main__":
    main()  # or some function call to start the app
