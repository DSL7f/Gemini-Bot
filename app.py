import streamlit as st
from openai import OpenAI

# Read the API key from Streamlit secrets
api_key = st.secrets["openai"]["api_key"]

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def get_response(user_input):
    completion = client.chat.completions.create(
        model="google/gemini-2.0-flash-001",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    return completion.choices[0].message.content

st.title("Chatbot")
st.write("Welcome to the chatbot! Type your message below and press Enter.")

user_input = st.text_input("You: ", "")

if user_input:
    response = get_response(user_input)
    st.write(f"Bot: {response}")