import streamlit as st
from googletrans import Translator, LANGUAGES

st.set_page_config(page_title="Multilingual Translator", layout="centered")
st.title("🌍 Multilingual AI Translator")

text = st.text_area("Enter text to translate:")

langs = list(LANGUAGES.values())

source_lang = st.selectbox("From Language:", langs, index=langs.index('english'))
target_lang = st.selectbox("To Language:", langs, index=langs.index('hindi'))

if st.button("Translate"):
    try:
        translator = Translator()
        source_code = list(LANGUAGES.keys())[langs.index(source_lang)]
        target_code = list(LANGUAGES.keys())[langs.index(target_lang)]
        result = translator.translate(text, src=source_code, dest=target_code)
        st.success(result.text)
    except Exception as e:
        st.error(f"Translation failed: {e}")
