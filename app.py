import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config import OPENAI_API_KEY

# Initialize the OpenAI model
llm = OpenAI(api_key=OPENAI_API_KEY)

# Define the prompt template for translation
prompt_template = PromptTemplate(
    input_variables=["text", "language"],
    template="Translate the following text to {language}: {text}",
)

# Create a chain using the prompt and LLM
translation_chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit app
st.set_page_config(page_title="Language Translation App", page_icon="🌐", layout="centered")

# Custom CSS to enhance appearance
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            color: #333;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
        }
        .stTextInput textarea {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }
        .stSelectbox select {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌐 Language Translation Web App")
st.write("Enter text in the source language and select the target language for translation.")
st.markdown("---")

# Text input from the user
source_text = st.text_area("📝 Source Text", "Type your text here...", height=150)

# Target language selection
target_language = st.selectbox(
    "🌍 Select Target Language",
    ("Spanish", "French", "German", "Chinese", "Japanese", "Korean")
)

st.markdown("---")

# Translate button
if st.button("Translate"):
    if source_text.strip() == "":
        st.error("Please enter some text to translate.")
    else:
        # Perform the translation using the LLMChain
        translation = translation_chain.run({"text": source_text, "language": target_language})

        # Display the translation with a nice card layout
        st.success("Translation:")
        st.markdown(f"""
            <div style="background-color: #e8f4e5; padding: 20px; border-radius: 8px; margin-top: 10px;">
                <h4 style="color: #4CAF50;">Translated Text:</h4>
                <p style="font-size: 18px; color: black;">{translation}</p>
            </div>
        """, unsafe_allow_html=True)

st.write("Powered by LangChain and OpenAI")
