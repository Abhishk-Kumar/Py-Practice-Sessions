from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
import os
api_key=os.getenv("api_key")

model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5, max_tokens=500, api_key=api_key)
 
st.header("Research Tool")
st.title("My Summarizer App : Sparkles")
prompt=st.text_input("Enter your paragraph to summarize it here")

if st.button("Summarize"):
    result=model.invoke(f"Summarized the following text : {prompt}")
    st.write(result.content)
