from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_jd_skills(jd_text, skill_list):
    jd_text = jd_text.lower()
    return [skill for skill in skill_list if skill in jd_text]

def skill_match_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0
    matched = set(resume_skills) & set(jd_skills)
    return round(len(matched) / len(jd_skills) * 100, 2)

def text_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(score[0][0] * 100, 2)

def skill_gap(resume_skills, jd_skills):
    return sorted(set(jd_skills) - set(resume_skills))