import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Buat client baru (versi OpenAI terbaru)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Chatbot Sekolah", layout="centered")
st.title("📚 AI Chatbot Pelajaran SD")

# Pilih pelajaran
subject = st.selectbox("Pilih pelajaran:", ["Umum", "PAI", "Matematika", "IPA", "Bahasa Indonesia"])

# Input pertanyaan
prompt_user = st.text_input("Tanya apa saja tentang pelajaran tersebut:")

if prompt_user:
    with st.spinner("Sedang berpikir..."):
        system_instruction = f"Kamu adalah guru SD yang pintar dan ramah. Jawablah dengan bahasa sederhana untuk anak-anak. Fokus pada pelajaran: {subject}."

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt_user}
            ],
            temperature=0.7,
            max_tokens=300
        )

        answer = response.choices[0].message.content
        st.success(answer)
