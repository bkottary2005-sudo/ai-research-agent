# AI Research Agent

An AI-powered research assistant that combines live web search with Google Gemini to generate structured, source-backed research reports.

## Overview

AI Research Agent helps users quickly research any topic by collecting current information from the web and using Google Gemini to transform the collected information into a structured research report.

The application is built with Python and Streamlit and integrates the Tavily Search API for web research and the Google Gemini API for AI-powered analysis and summarization.

## Features

- Live web search using Tavily
- AI-powered research using Google Gemini
- Automated research report generation
- Structured reports with:
  - Overview
  - Key Findings
  - Important Insights
  - Applications
  - Future Scope
  - References
- Source links for researched information
- Research progress indicators
- Research statistics
- Download generated reports as Markdown
- Research history
- Clean and responsive Streamlit interface
- Environment variable support for API keys

## How It Works

```text
User enters research topic
          |
          v
     Streamlit UI
          |
          v
     Tavily Web Search
          |
          v
   Relevant Web Sources
          |
          v
    Google Gemini AI
          |
          v
 Structured Research Report
          |
          +----------------+
          |                |
          v                v
    Report Display     References
          |
          v
