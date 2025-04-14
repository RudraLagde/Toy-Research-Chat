from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 

st.title('Research Bot')

load_dotenv()

model = GoogleGenerativeAI(model='gemini-flash-2.0')

user_input = st.text_input('Input the paper you want summary of')

if st.button('Submit'):
    result= model.invoke(user_input)
    print(result)