import openai
from dotenv import load_dotenv
import os
import streamlit as st

# Load your OpenAI API key from an environment variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openAI_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message['content']

st.set_page_config(page_title="Answer")
st.header("Langchain Application")

user_input = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

if submit and user_input:
    response = get_openAI_response(user_input)
    st.subheader("The response is:")
    st.write(response)
