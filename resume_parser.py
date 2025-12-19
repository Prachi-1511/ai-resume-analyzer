import re
import pdfplumber
import spacy
from skills import SKILLS

nlp = spacy.load("en_core_web_sm")

def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group() if match else "Not Found"

def extract_phone(text):
    match = re.search(r'\b\d{10}\b', text)
    return match.group() if match else "Not Found"

def extract_skills(text):
    return sorted(set(skill for skill in SKILLS if skill in text))

def extract_experience(text):
    patterns = [
        r'\b\d+\+?\s+years?\b',
        r'\binternship\b',
        r'\bexperience\b'
    ]
    return any(re.search(p, text) for p in patterns)

def parse_resume(pdf_file):
    text = extract_text(pdf_file)
    return {
        "text": text,
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text)
    }