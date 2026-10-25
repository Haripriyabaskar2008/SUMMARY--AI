
import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("AI Text Summarizer")
st.caption("Summarize long text instantly using Google Gemini AI")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key missing. Add it to your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

text = st.text_area(
    "Enter your text",
    height=300,
    placeholder="Paste an article, notes, or a long paragraph here..."
)

length = st.selectbox(
    "Choose summary length",
    ["Short", "Medium", "Detailed"]
)

if st.button("Generate Summary", type="primary"):
    if not text.strip():
        st.warning("Please enter some text first.")

    else:
        instructions = {
            "Short": "Summarize in 3 to 5 sentences.",
            "Medium": "Summarize in one concise paragraph.",
            "Detailed": "Create a detailed summary with key points."
        }

        prompt = f"""
        You are an expert text summarization assistant.
        Summarize the following text accurately.
        Preserve the important facts and main ideas.
        Do not add information that is not in the text.
        {instructions[length]}

        TEXT:
        {text}
        """

        try:
            with st.spinner("Generating your summary..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

            if response.text:
                st.subheader("Generated Summary")
                st.write(response.text)

                st.download_button(
                    "Download Summary",
                    data=response.text,
                    file_name="summary.txt",
                    mime="text/plain"
                )
            else:
                st.error("No summary returned. Please try again.")

        except Exception as e:
            st.error(f"Unable to generate summary: {e}")
