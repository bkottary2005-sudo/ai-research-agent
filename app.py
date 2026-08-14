import time
import streamlit as st

from utils.search import search_web
from utils.summarize import generate_summary


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="AI",
    layout="wide"
)


# ---------------------------------------------------------
# Load Custom CSS
# ---------------------------------------------------------

def load_css():
    try:
        with open("assets/style.css", encoding="utf-8") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass


load_css()


# ---------------------------------------------------------
# Research History
# ---------------------------------------------------------

if "research_history" not in st.session_state:
    st.session_state.research_history = []


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.title("AI Research Agent")

    st.markdown("---")

    st.subheader("Overview")

    st.write(
        """
AI Research Agent combines live web search with Google Gemini AI
to generate structured research reports using current information
from online sources.
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

    st.subheader("Research History")

    if st.session_state.research_history:

        for item in st.session_state.research_history:

            st.markdown(
                f"**{item['topic']}**"
            )

            st.caption(
                f"{item['sources']} sources"
            )

            st.markdown("---")

    else:

        st.caption("No research reports generated yet.")

    if st.session_state.research_history:

        if st.button("Clear History", use_container_width=True):

            st.session_state.research_history = []

            st.rerun()

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
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# Initial Statistics
# ---------------------------------------------------------

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric("Search Engine", "Tavily")

with metric2:
    st.metric("AI Model", "Gemini")

with metric3:
    st.metric(
        "Reports",
        len(st.session_state.research_history)
    )


st.divider()


# ---------------------------------------------------------
# Research Input
# ---------------------------------------------------------

topic = st.text_input(
    "Research Topic",
    placeholder="Example: Agentic AI, Quantum Computing, NVIDIA AI..."
)


# ---------------------------------------------------------
# Generate Research Report
# ---------------------------------------------------------

if st.button("Generate Report", use_container_width=True):

    if not topic.strip():

        st.warning("Please enter a research topic.")

    else:

        try:

            progress = st.progress(0)
            status = st.empty()

            # ---------------------------------------------
            # Web Search
            # ---------------------------------------------

            status.info("Searching the web...")
            progress.progress(20)

            results = search_web(topic)

            # ---------------------------------------------
            # Read Sources
            # ---------------------------------------------

            progress.progress(45)
            status.info("Analyzing research sources...")

            time.sleep(0.5)

            # ---------------------------------------------
            # Generate AI Report
            # ---------------------------------------------

            progress.progress(65)
            status.info("Generating research report...")

            summary = generate_summary(
                topic,
                results
            )

            # ---------------------------------------------
            # Complete
            # ---------------------------------------------

            progress.progress(100)

            time.sleep(0.3)

            status.empty()
            progress.empty()

            # ---------------------------------------------
            # Handle AI Response
            # ---------------------------------------------

            if summary.startswith("⚠️"):

                st.warning(summary)

            else:

                st.success(
                    "Research report generated successfully."
                )

                # -----------------------------------------
                # Save Research History
                # -----------------------------------------

                history_item = {
                    "topic": topic,
                    "summary": summary,
                    "sources": len(results)
                }

                st.session_state.research_history.insert(
                    0,
                    history_item
                )

                # Keep only the latest 5 reports
                st.session_state.research_history = (
                    st.session_state.research_history[:5]
                )

                # -----------------------------------------
                # Download Report
                # -----------------------------------------

                st.download_button(
                    label="Download Report",
                    data=summary,
                    file_name=f"{topic.replace(' ', '_')}_research.md",
                    mime="text/markdown"
                )

                st.markdown("---")

                # -----------------------------------------
                # Research Report
                # -----------------------------------------

                st.subheader("Research Report")

                st.markdown(summary)

            # ---------------------------------------------
            # Sources
            # ---------------------------------------------

            st.markdown("---")

            st.subheader("Research Sources")

            for i, result in enumerate(
                results,
                start=1
            ):

                with st.expander(
                    f"{i}. {result['title']}"
                ):

                    st.write(
                        result["content"]
                    )

                    st.link_button(
                        "View Source",
                        result["url"],
                        use_container_width=True
                    )

            # ---------------------------------------------
            # Report Statistics
            # ---------------------------------------------

            st.markdown("---")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Sources Used",
                    len(results)
                )

            with col2:

                st.metric(
                    "Words",
                    len(summary.split())
                )

            with col3:

                st.metric(
                    "Reports",
                    len(st.session_state.research_history)
                )

        except Exception as e:

            st.error(
                f"An unexpected error occurred.\n\n{e}"
            )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;color:#6B7280;font-size:14px;padding:20px;">

AI Research Agent

<br>

Developed by <b>Bhoomika K Kottary</b>

</div>
""",
    unsafe_allow_html=True
)