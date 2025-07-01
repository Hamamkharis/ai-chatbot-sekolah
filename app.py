import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

st.set_page_config(page_title="AI Chatbot Sekolah", layout="centered")
st.title("📚 AI Chatbot Pelajaran SD")

subject = st.selectbox("Pilih pelajaran:", ["Umum", "PAI", "Matematika", "IPA", "Bahasa Indonesia"])
prompt_user = st.text_input("Tanya apa saja tentang pelajaran tersebut:")

if prompt_user:
    with st.spinner("Sedang berpikir..."):
        system_msg = f"Kamu adalah guru SD yang pintar dan ramah. Jawablah dengan bahasa sederhana untuk anak-anak. Fokus pada pelajaran: {subject}."
        payload = {
            "model": "meta-llama/Llama-3-70b-chat-hf",
            "messages": [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt_user}
            ],
            "temperature": 0.7,
            "max_tokens": 300
        }

        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=payload)
        result = response.json()
        try:
            answer = result["choices"][0]["message"]["content"]
            st.success(answer)
        except Exception as e:
            st.error("Terjadi kesalahan: " + str(e))
