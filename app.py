import streamlit as st
import pandas as pd

from resume_parser import parse_resume
from jd_matcher import extract_jd_skills, skill_match_score, text_similarity, skill_gap
from scoring import final_score, verdict
from skills import SKILLS

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI-Powered Resume Screening System")
st.caption("Automated resume parsing, ranking, and JD matching")

st.divider()

# Inputs
resumes = st.file_uploader(
    "Upload Resume PDFs (Multiple Allowed)",
    type="pdf",
    accept_multiple_files=True
)

jd_text = st.text_area("Paste Job Description", height=200)

if resumes and jd_text:
    jd_skills = extract_jd_skills(jd_text, SKILLS)

    results = []

    for resume in resumes:
        parsed = parse_resume(resume)

        skill_score = skill_match_score(parsed["skills"], jd_skills)
        similarity = text_similarity(parsed["text"], jd_text)
        final = final_score(skill_score, similarity, parsed["experience"])

        results.append({
            "Candidate": resume.name,
            "Final Score (%)": final,
            "Skill Match (%)": skill_score,
            "JD Similarity (%)": similarity,
            "Experience": "Yes" if parsed["experience"] else "No",
            "Verdict": verdict(final),
            "Skills": ", ".join(parsed["skills"]),
            "Missing Skills": ", ".join(skill_gap(parsed["skills"], jd_skills))
        })

    df = pd.DataFrame(results).sort_values("Final Score (%)", ascending=False).reset_index(drop=True)
    df.index += 1

    st.subheader("📊 Candidate Ranking")
    st.dataframe(df, use_container_width=True)

    st.divider()

    st.subheader("🔍 Detailed Candidate Analysis")
    for i, row in df.iterrows():
        with st.expander(f"#{i} — {row['Candidate']} ({row['Verdict']})"):
            st.write("**Final Score:**", row["Final Score (%)"])
            st.write("**Skill Match:**", row["Skill Match (%)"])
            st.write("**JD Similarity:**", row["JD Similarity (%)"])
            st.write("**Experience Detected:**", row["Experience"])
            st.write("**Skills:**", row["Skills"])
            st.write("**Missing Skills:**", row["Missing Skills"])

else:
    st.info("Upload resumes and paste a job description to start analysis.")
