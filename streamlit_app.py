import streamlit as st
from app.groq_llm import get_llm
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Groq Chatbot")

# ---- Initialize chat history ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- Show previous messages ----
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---- User input ----
user_input = st.chat_input("Ask something...")

# ---- PROCESS ONLY WHEN USER SENDS MESSAGE ----
if user_input:

    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Convert history → LC format
    lc_history = []
    for m in st.session_state.messages:
        if m["role"] == "user":
            lc_history.append(HumanMessage(content=m["content"]))
        else:
            lc_history.append(AIMessage(content=m["content"]))

    # ---- Call Groq LLM now (NOT before user input) ----
    llm = get_llm()
    response = llm.invoke(lc_history)
    assistant_text = response.content

    # Add assistant answer
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_text}
    )

    # Show assistant message
    with st.chat_message("assistant"):
        st.write(assistant_text)
