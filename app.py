import streamlit as st
from utils.search import search_web
from utils.summarize import generate_summary

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Research Agent")

st.write(
    "Research any topic using **live web search** and **AI-powered summarization**."
)

st.divider()

topic = st.text_input(
    "🔍 Enter a research topic",
    placeholder="Example: Agentic AI, Quantum Computing, Climate Change"
)

if st.button("🚀 Start Research", use_container_width=True):

    if not topic.strip():
        st.warning("⚠️ Please enter a research topic.")

    else:
        try:
            # Search the web
            with st.spinner("🔎 Searching the web..."):
                results = search_web(topic)

            # Generate summary
            with st.spinner("🤖 Generating AI research report..."):
                summary = generate_summary(topic, results)

            # Display summary
            if summary.startswith("⚠️"):
                st.warning(summary)
            else:
                st.success("✅ Research Complete!")
                st.markdown(summary)

            # Sources
            st.divider()
            st.subheader("🌐 Sources")

            for result in results:
                st.markdown(f"**[{result['title']}]({result['url']})**")
                st.caption(result["url"])

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")