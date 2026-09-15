import os
import json
import traceback

import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utills import read_file, get_table_data
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from src.mcqgenerator.logger import logging
load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


#creating a title for the app
st.title("MCQ Generator using Gemini and Langchain")

with st.form("my_form"):
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

    number = st.number_input("Number of MCQs to generate", min_value=1, max_value=50, value=3, step=1, key="num_mcqs")   

    subject = st.text_input("Enter the subject for the MCQs", value="General Knowledge", key="subject") 

    tone= st.selectbox("Select the tone for the MCQs", ["Formal", "Informal", "Humorous", "Serious"], key="tone")   

    submit_button = st.form_submit_button(label="Generate MCQs")
    if submit_button and uploaded_file is not None and number  is not None and subject is not None and tone is not None:
        with st.spinner("Generating MCQs..."):
            try:
                # Read the uploaded file
                text = read_file(uploaded_file)

                # Get the number of MCQs to generate
                num_mcqs = st.session_state.num_mcqs

                # Get the subject for the MCQs
                subject = st.session_state.subject

                # Get the tone for the MCQs
                tone = st.session_state.tone

                # Generate MCQs using Gemini and Langchain
                llm = ChatGoogleGenerativeAI(
                    model="gemini-3.7-flash",
                    google_api_key=os.getenv("genai_api_key"),
                    temperature=0.5
                )

                prompt_template = PromptTemplate(
                    input_variables=["text", "num_mcqs", "subject", "tone"],
                    template="""
                    You are an expert in generating multiple choice questions (MCQs) based on the provided text.
                    Generate {num_mcqs} MCQs on the subject of {subject} with a {tone} tone.
                    Text: {text}
                    """,
                )

                prompt = prompt_template.format(
                    text=text,
                    num_mcqs=num_mcqs,
                    subject=subject,
                    tone=tone
                )

                response = llm.invoke(prompt)
                st.write(response.content)

                # Display the generated MCQs
                st.subheader("Generated MCQs")
                st.write(response)

            except Exception as e:
                logging.error(f"Error generating MCQs: {e}")
                st.error(f"Error generating MCQs: {e}")
