from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import load_prompt

st.title('Research Bot')

load_dotenv()

model = GoogleGenerativeAI(model='gemini-2.0-flash')

paper_input = st.text_input('Insert Research Paper you want to summarize')
style_input = st.selectbox('Select the summary tone',['Begginer','Intermediate','Advanced'])
length_input = st.selectbox('Select the summary length',['Small 30-40 words','Medium 60-70 words','Long 80+ words'])


template = load_prompt('template.json')


if st.button('Summarize'):
    chain = template | model        
    result = chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input })
    st.write(result)