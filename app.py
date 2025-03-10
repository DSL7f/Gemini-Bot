# filepath: c:\Users\USER\Documents\.VS Code\Gemini Bot W\chatbot-project\src\app.py
import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your_actual_api_key_here",
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