import chromadb
import requests
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text: str, chunk_size: int = 700, overlap: int = 100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def create_collection(resume_text: str, jd_text: str):
    client = chromadb.Client()

    try:
        client.delete_collection("resume_analysis")
    except:
        pass

    collection = client.create_collection("resume_analysis")

    resume_chunks = chunk_text(resume_text)
    jd_chunks = chunk_text(jd_text)

    all_chunks = []

    for chunk in resume_chunks:
        all_chunks.append(("resume", chunk))

    for chunk in jd_chunks:
        all_chunks.append(("job_description", chunk))

    for i, (source, chunk) in enumerate(all_chunks):
        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{"source": source}]
        )

    return collection


def retrieve_context(collection, query: str, top_k: int = 5):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    docs = results["documents"][0]
    return "\n\n".join(docs)


def call_ollama(prompt: str):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"]

    except Exception as e:
        return f"Ollama error: {str(e)}"


def generate_resume_analysis(resume_text: str, jd_text: str, ats_data: dict):
    collection = create_collection(resume_text, jd_text)

    query = """
    Analyze resume against job description.
    Find strengths, weaknesses, missing skills, improvement suggestions,
    and interview questions.
    """

    context = retrieve_context(collection, query)

    prompt = f"""
You are an expert ATS resume analyzer and career coach.

Use the given context to analyze the resume against the job description.

ATS DATA:
Score: {ats_data['score']}
Matched Skills: {ats_data['matched_skills']}
Missing Skills: {ats_data['missing_skills']}

CONTEXT:
{context}

Give output in this exact format:

SUMMARY:
Write a short summary.

STRENGTHS:
- point 1
- point 2
- point 3

WEAKNESSES:
- point 1
- point 2
- point 3

RESUME IMPROVEMENT SUGGESTIONS:
- point 1
- point 2
- point 3
- point 4
- point 5

PROJECT IMPROVEMENT IDEAS:
- point 1
- point 2
- point 3

INTERVIEW QUESTIONS:
1. question
2. question
3. question
4. question
5. question

FINAL VERDICT:
Give final hiring readiness verdict.
"""

    return call_ollama(prompt)