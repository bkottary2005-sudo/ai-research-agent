import time
import streamlit as st

from utils.search import search_web
from utils.summarize import generate_summary


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="📄",
    layout="wide"
)


# ---------------------------------------------------------
# Load CSS
# ---------------------------------------------------------

def load_css():
    try:
        with open("assets/style.css") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass


load_css()


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.title("AI Research Agent")

    st.markdown("---")

    st.subheader("Overview")

    st.write(
        """
AI Research Agent is an intelligent research assistant
that combines live web search with Google Gemini AI to
generate structured research reports from current information.
"""
    )

    st.markdown("---")

    st.subheader("Technology")

    st.markdown(
        """
- Python
- Streamlit
- Google Gemini API
- Tavily Search API
"""
    )

    st.markdown("---")

    st.subheader("Developer")

    st.write("**Bhoomika K Kottary**")

    st.markdown("---")

    st.success("System Online")


# ---------------------------------------------------------
# Hero Section
# ---------------------------------------------------------

st.markdown(
    """
<div style="padding-top:10px;padding-bottom:20px;">

<h1 style="font-size:48px;margin-bottom:5px;">
AI Research Agent
</h1>

<p style="font-size:18px;color:#6b7280;">
Generate professional research reports using live web search
and Google Gemini AI.
</p>

</div>
""",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Statistics
# ---------------------------------------------------------

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric("Search Engine", "Tavily")

with metric2:
    st.metric("AI Model", "Gemini")

with metric3:
    st.metric("Status", "Ready")


st.divider()


# ---------------------------------------------------------
# Input
# ---------------------------------------------------------

topic = st.text_input(
    "Research Topic",
    placeholder="Example: Agentic AI, Quantum Computing, NVIDIA AI..."
)


# ---------------------------------------------------------
# Generate
# ---------------------------------------------------------

if st.button("Generate Report", use_container_width=True):

    if topic.strip() == "":

        st.warning("Please enter a research topic.")

    else:

        try:

            progress = st.progress(0)

            status = st.empty()

            status.info("Searching the web...")
            progress.progress(20)

            results = search_web(topic)

            progress.progress(45)

            status.info("Reading sources...")

            time.sleep(0.5)

            progress.progress(65)

            status.info("Generating research report...")

            summary = generate_summary(topic, results)

            progress.progress(100)

            status.empty()
            progress.empty()

            if summary.startswith("⚠️"):

                st.warning(summary)

            else:

                st.success("Research report generated successfully.")

                st.download_button(
                    "Download Report",
                    summary,
                    file_name=f"{topic}.md",
                    mime="text/markdown"
                )

                st.markdown("---")

                st.markdown(summary)

            st.markdown("---")

            st.subheader("Research Sources")

            for i, result in enumerate(results, start=1):

                with st.expander(f"{i}. {result['title']}"):

                    st.write(result["content"])

                    st.link_button(
                        "View Source",
                        result["url"],
                        use_container_width=True,
                    )

            st.markdown("---")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Sources Used", len(results))

            with col2:
                st.metric(
                    "Words",
                    len(summary.split())
                )

            with col3:
                st.metric(
                    "Report",
                    "Generated"
                )

        except Exception as e:

            st.error(f"Error: {e}")


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;color:gray;font-size:14px;padding:20px;">

AI Research Agent

Developed by <b>Bhoomika K Kottary</b>

</div>
""",
    unsafe_allow_html=True,
)