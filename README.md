# 🚀 AI Resume Analyzer

**Make your resume job-ready with AI-powered insights.**

An AI-powered resume analysis tool that compares your resume with a job description using **RAG, LLaMA 3, and semantic search**. It helps identify matching skills, missing skills, and areas for improvement.

## ✨ Features

* 📄 **Resume Analysis** – Upload your resume in PDF format.
* 🎯 **ATS Score** – Get a skill-based match score.
* ✅ **Skill Matching** – Identify matched and missing skills.
* 🧠 **AI-Powered Insights** – Analyze strengths and weaknesses.
* 💡 **Smart Suggestions** – Get recommendations to improve your resume.
* 🔍 **RAG-Based Retrieval** – Retrieve relevant resume and job description context.

## 🛠️ Tech Stack

**Frontend:** React, Tailwind CSS, Axios, Framer Motion
**Backend:** Python, FastAPI
**AI/ML:** LLaMA 3, Sentence Transformers
**Vector Database:** ChromaDB
**PDF Processing:** PyMuPDF
**LLM Runtime:** Ollama

## ⚙️ How It Works

1. Upload your resume and enter the job description.
2. Extract and split the text into smaller chunks.
3. Generate embeddings using Sentence Transformers.
4. Store and retrieve relevant information using ChromaDB.
5. Pass the retrieved context to LLaMA 3 through Ollama.
6. View your ATS score and AI-generated analysis.

## 🏗️ Architecture

```text
Resume + Job Description
          ↓
     Text Extraction
          ↓
        Chunking
          ↓
      Embeddings
          ↓
       ChromaDB
          ↓
    Context Retrieval
          ↓
       LLaMA 3
          ↓
   Resume Analysis
```

## 🚀 Getting Started

### Prerequisites

* Python
* Node.js
* Ollama

### Run the Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Run Ollama

```bash
ollama run llama3
```

### Run the Frontend

```bash
cd frontend
npm install
npm run dev
```

## 📌 Project Highlights

* Combines traditional skill-based ATS scoring with RAG-based AI analysis.
* Uses semantic embeddings to retrieve relevant context.
* Runs LLaMA 3 locally through Ollama.

## 🔮 Future Enhancements

* Support for more resume formats.
* Improved skill extraction and matching.
* Enhanced retrieval and analysis accuracy.
* Deployment as a cloud-based application.

---

**Built with Python, React, and Generative AI.**
