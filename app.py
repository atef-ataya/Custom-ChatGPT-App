from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

# Applicaiton Layout

st.set_page_config(
    page_title="Personal Assitant",
    page_icon=":full_moon_with_face:"
)

st.subheader("Language Chain - Chat App")

chat = ChatOpenAI(model_name='gpt-4-turbo-preview', temperature=0.5)

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    system_message = st.text_input(label="System Role")
    user_prompt = st.text_input(label="Please enter your query")

    if system_message:
        if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
            st.session_state.messages.append(SystemMessage(content=system_message))

        # st.write(st.session_state.messages)

    if user_prompt:
        st.session_state.messages.append(
            HumanMessage(content=user_prompt)
        )

        with st.spinner("Working on your request ..."):
            response = chat(st.session_state.messages)

        st.session_state.messages.append(AIMessage(content=response.content))

# st.session_state.messages
# message('This is a Chatgpt', is_user=False)
# message('This is the user', is_user=True)
if len(st.session_state.messages) >= 1:
    if not isinstance(st.session_state.messages[0], SystemMessage):
        st.session_state.messages.insert(0, SystemMessage(content='You are my helpful asistent'))

for i, msg in enumerate(st.session_state.messages[1:]):
    if i % 2 == 0:
        message(msg.content, is_user=True, key=f'{i} + :earth_americas:')
    else:
        message(msg.content, is_user=False, key=f'{i} + :europe:')





