# app.py
import streamlit as st
from transformers import pipeline


chat_model = pipeline("conversational")


st.title("Document Search and Chat with LLM")

if 'messages' not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

prompt=st.chat_input('Pass Your Prompt here')

if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role':'user','content':prompt})

