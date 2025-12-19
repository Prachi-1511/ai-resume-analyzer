# AI-Powered Resume Screening & Candidate Ranking System

An end-to-end resume screening system that parses resumes, extracts skills and experience, and ranks candidates against a given job description using NLP and similarity scoring.

This project simulates real-world hiring workflows used in enterprise recruitment platforms.

---

## Features
- Multi-resume upload and automated ranking
- Resume parsing using NLP and regex
- Skill extraction and skill gap analysis
- Resume–JD similarity using TF-IDF and cosine similarity
- Weighted scoring system with recruiter-style verdicts
- Interactive web interface built with Streamlit

---

## Scoring Logic

| Component | Weight |
|---------|--------|
| Skill Match | 50% |
| Resume–JD Similarity | 30% |
| Experience Indicator | 20% |

Final score is capped at **100%** and mapped to:
- **Strong Fit**
- **Partial Fit**
- **Weak Fit**

---

## Project Architecture
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

## Tech Stack
- Python
- spaCy (NLP)
- Regex
- TF-IDF & Cosine Similarity
- Streamlit
- pdfplumber
- scikit-learn

## Installation & Run

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py