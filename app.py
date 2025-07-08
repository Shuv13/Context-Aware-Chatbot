import os
import streamlit as st
from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

# Supported languages
SUPPORTED_LANGS = {
    "en": "English",
    "hi": "Hindi",
    "bn": "Bengali"
}

st.set_page_config(page_title="Multilingual Groq Chatbot", layout="centered")
st.title("🧠 Nora - Multilingual Groq Chatbot")

st.sidebar.header("🔐 API & Settings")
api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")

selected_model = st.sidebar.selectbox(
    "Select a model:",
    [
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mixtral-8x7b-32768",
        "gemma-7b-it",
        "gemma-2b-it"
    ],
    index=0
)


selected_lang = st.sidebar.selectbox(
    "Select language:",
    list(SUPPORTED_LANGS.keys()),
    index=0,
    format_func=lambda x: f"{SUPPORTED_LANGS[x]} ({x})"
)

if api_key:
    os.environ["GROQ_API_KEY"] = api_key

    if "groq_model" not in st.session_state:
        st.session_state["groq_model"] = selected_model

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history", return_messages=True)

    for msg in st.session_state.chat_history:
        memory.save_context({"input": msg["human"]}, {"output": msg["AI"]})

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Type your message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Language-specific instructions
        system_prompt = (
            f"You are a helpful assistant. Respond strictly in {SUPPORTED_LANGS[selected_lang]}.\n"
            f"If user input is in another language, translate and respond in {SUPPORTED_LANGS[selected_lang]} only."
        )

        chat_prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{human_input}")
            ]
        )

        groq_chat = ChatGroq(groq_api_key=api_key, model_name=selected_model)

        conversation = LLMChain(
            llm=groq_chat,
            prompt=chat_prompt,
            memory=memory,
            verbose=False
        )

        response = conversation.predict(human_input=prompt)

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.chat_history.append({"human": prompt, "AI": response})

else:
    st.error("Please enter your Groq API key to start chatting.")
