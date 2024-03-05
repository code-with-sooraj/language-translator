import streamlit as st
from googletrans import Translator

translator = Translator()

def translate_text(text, dest_language):
    translated = translator.translate(text, dest=dest_language)
    return translated.text

st.title("Language Translator")

user_input = st.text_input("Enter text to translate:")
dest_language = st.selectbox("Select destination language:", ["af", "ar", "bg", "bn", "bs", "ca", "cs", "da", "de", "el", "en", "es", "et", "eu", "fa", "fi", "fr", "ga", "gu", "he", "hi", "hr", "hu", "id", "is", "it", "ja", "jw", "ka", "kk", "km", "kn", "ko", "cs", "da", "de", "el", "en", "es", "et", "eu", "fa", "fi", "fr", "ga", "gd", "gl", "gu", "ha", "he", "hi", "hr", "hu", "hy", "id", "ig", "is", "it", "ja", "jw", "ka", "kk", "km", "kn", "ko", "lo", "lt", "lv", "mi", "mk", "ml", "mn", "mr", "ms", "mt", "my", "ne", "nl", "no", "ps", "pt", "ro", "ru", "sd", "si", "sk", "sl", "sm", "sn", "so", "sq", "sr", "ss", "st", "su", "sv", "sw", "ta", "te", "tg", "th", "ti", "tk", "tl", "tn", "to", "tr", "uk", "ur", "uz", "vi", "xh", "yi", "yo", "zh", "zu"])

if st.button("Translate"):
    translated_text = translate_text(user_input, dest_language)
    st.write("Translated text:")
    st.write(translated_text)