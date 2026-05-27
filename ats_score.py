import re


COMMON_SKILLS = [
    "python", "java", "c++", "sql", "machine learning", "deep learning",
    "nlp", "data science", "pandas", "numpy", "tensorflow", "pytorch",
    "fastapi", "flask", "django", "react", "node.js", "mongodb",
    "postgresql", "mysql", "aws", "azure", "docker", "kubernetes",
    "git", "github", "linux", "html", "css", "javascript",
    "typescript", "api", "rest api", "rag", "llm", "langchain",
    "chromadb", "opencv", "computer vision"
]


def clean_text(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9+#. ]", " ", text.lower())


def extract_skills(text: str):
    cleaned = clean_text(text)
    found = []

    for skill in COMMON_SKILLS:
        if skill in cleaned:
            found.append(skill)

    return sorted(list(set(found)))


def calculate_ats_score(resume_text: str, jd_text: str):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    if not jd_skills:
        return {
            "score": 50,
            "matched_skills": resume_skills,
            "missing_skills": [],
            "jd_skills": []
        }

    matched = [skill for skill in jd_skills if skill in resume_skills]
    missing = [skill for skill in jd_skills if skill not in resume_skills]

    score = int((len(matched) / len(jd_skills)) * 100)

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "jd_skills": jd_skills
    }