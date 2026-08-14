# AI Research Agent

An AI-powered research assistant that combines live web search with Google Gemini to generate structured and source-backed research reports.

The application searches the web for current information, analyzes the collected sources using Gemini, and presents the findings in a clean Streamlit interface.

---

## Overview

Traditional AI chat applications often rely only on the model's existing knowledge.

This project takes a different approach by combining:

- Live web search
- AI-powered analysis
- Automated summarization
- Source references
- Research report generation

The result is an end-to-end research workflow that can be used to quickly explore technical, scientific, business, and general topics.

---

## Features

### Live Web Research

Uses the Tavily Search API to retrieve current information from the web.

### AI-Powered Analysis

Google Gemini analyzes the collected research material and generates a structured report.

### Structured Research Reports

Reports are organized into sections such as:

- Overview
- Key Findings
- Important Insights
- Applications
- Future Scope
- References

### Source References

The application displays the sources used during the research process with links to the original articles.

### Research Progress

The interface provides visual progress updates while:

1. Searching the web
2. Analyzing sources
3. Generating the report

### Report Download

Generated reports can be downloaded as Markdown files.

### Research History

The application maintains recent research topics during the session.

### Professional Streamlit Interface

The application includes:

- Responsive layout
- Sidebar navigation
- Research statistics
- Expandable source sections
- Custom CSS styling
- Clean research dashboard

---

## Architecture

```text
                    User
                     |
                     v
              Research Topic
                     |
                     v
              Streamlit UI
                     |
                     v
              Tavily Search
                     |
                     v
             Web Search Results
                     |
                     v
             Google Gemini AI
                     |
                     v
           Research Report
                     |
          +----------+----------+
          |                     |
          v                     v
     Report Display        Source Links
          |
          v
    Markdown Download
