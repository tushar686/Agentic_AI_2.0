
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

#Langsmith Tracking And Tracing
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")
os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")

import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


llm = ChatGroq(model="gemma2-9b-it")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant answering user question"),
        ("user", "Question: {question}")
    ]
)

parser = StrOutputParser()
chain = prompt | llm | parser

st.title("ChatBot")
input = st.text_input("Question")

resp = chain.invoke({"question": input})
st.write(resp)
