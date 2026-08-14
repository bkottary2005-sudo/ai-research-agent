import streamlit as st
from utils.summarize import generate_summary

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Research Agent")

st.write(
    "Welcome! This AI agent will research any topic and generate a concise summary."
)

st.divider()

topic = st.text_input(
    "🔍 Enter a research topic",
    placeholder="Example: Agentic AI, Quantum Computing, Climate Change"
)

if st.button("🚀 Start Research", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a research topic.")

    else:

        with st.spinner("🤖 Researching... Please wait..."):

            summary = generate_summary(topic)

        st.success("Research Completed!")

        st.markdown(summary)