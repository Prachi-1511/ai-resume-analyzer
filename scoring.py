def final_score(skill_score, similarity_score, experience):
    score = (0.5 * skill_score) + (0.3 * similarity_score)
    if experience:
        score += 20
    return min(round(score, 2), 100)

def verdict(score):
    if score >= 75:
        return "Strong Fit"
    elif score >= 50:
        return "Partial Fit"
    return "Weak Fit"