from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 

st.title('Research Bot')

load_dotenv()

model = GoogleGenerativeAI(model='gemini-2.0-flash')

user_input = st.text_input('Insert Research Paper you want to summarize')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result)