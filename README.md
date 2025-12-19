# AI-Powered Resume Screening & Candidate Ranking System

## Overview
This project implements an end-to-end AI-based resume screening system that simulates real-world hiring workflows.
It automatically parses resumes, extracts skills and experience, and ranks candidates against a given job description using NLP-based similarity scoring.

The system is designed to reflect how modern recruitment platforms assist recruiters in efficient candidate shortlisting.

## Features
- Upload and analyze multiple resumes
- Resume parsing using NLP and regex-based extraction
- Skill extraction and skill gap analysis
- Resume–Job Description similarity using **TF-IDF and cosine similarity**
- Weighted scoring system with recruiter-style verdicts
- Interactive web interface built using **Streamlit**

## Scoring Logic
Each candidate is scored out of **100** using weighted components:

| Component | Weight |
|---------|--------|
| Skill Match | 50% |
| Resume–JD Similarity | 30% |
| Experience Indicator | 20% |

Final verdicts:
- **Strong Fit**
- **Partial Fit**
- **Weak Fit**

## Tech Stack
Python, spaCy (NLP), Regex, TF-IDF & Cosine Similarity, Streamlit, pdfplumber, scikit-learn

## System Workflow

Resume PDF
    ↓
Text Extraction
    ↓
Skill & Experience Extraction
    ↓
Job Description Processing
    ↓
Similarity & Weighted Scoring
    ↓
Candidate Ranking

## Installation & Run
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py