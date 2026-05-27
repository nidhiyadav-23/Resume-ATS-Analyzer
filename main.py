import os
import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from resume_parser import extract_text_from_pdf
from ats_score import calculate_ats_score
from rag_engine import generate_resume_analysis


app = FastAPI(title="AI Resume Analyzer RAG")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer RAG Backend Running"
    }


@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    file_path = os.path.join(UPLOAD_DIR, resume.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    resume_text = extract_text_from_pdf(file_path)

    ats_data = calculate_ats_score(resume_text, job_description)

    ai_analysis = generate_resume_analysis(
        resume_text=resume_text,
        jd_text=job_description,
        ats_data=ats_data
    )

    return {
        "ats_score": ats_data["score"],
        "matched_skills": ats_data["matched_skills"],
        "missing_skills": ats_data["missing_skills"],
        "jd_skills": ats_data["jd_skills"],
        "analysis": ai_analysis
    }