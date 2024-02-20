from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
os.environ["OPENAI_API_KEY"]= "#insert your own openai API key"

import streamlit as st

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], model_name="gpt-3.5-turbo-instruct", temperature=0.6)
    response = llm(question)
    return response
    
#initalize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input =st.text_input("Input: ", key ="input")
response = get_openai_response(input)

submit= st.button("Ask the quesion")
if submit:
    st.subheader("Answer :")
    st.write(response)
