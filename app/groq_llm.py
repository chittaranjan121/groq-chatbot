import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=st.secrets["GROQ_API_KEY"],
        #groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2
    )