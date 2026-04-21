
# 🚀 Legal AI System (Production-Grade RAG)

## 🔥 Features
- Hybrid Retrieval (FAISS + BM25)
- Cross-Encoder Reranking
- Grounded Legal Drafting with Citations
- Feedback Learning Loop
- Evaluation Pipeline
- FastAPI Backend
- Docker + One Command Run
- Ready for real legal messy documents

---

**Sample query and responses saved to "./data/sample_response_file.txt"**

## ⚡ Quick Start

### 1. Clone
```bash
git clone https://github.com/mdhasanali3/Legal-case-AI.git
cd legal_ai_system
```
#### 1.1 Set up environment 
```bash
python -m venv venv
venv\scripts\activate

pip install -r requirements.txt
```

### 2. Run locally
Rename env file then insert openai key in the env file.
```bash
uvicorn run main:app --reload
```
### 2. Run with Docker (skip 1.1 step)
```bash
docker build -t legal-ai .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key legal-ai
```

### 3. API
- POST /query
- POST /feedback

---

## 🧠 Architecture
- Ingestion → Chunking → Embeddings
- Hybrid Retrieval → Reranking
- Context Builder → LLM Draft
- Evaluation → Feedback Loop

---

## 📊 Evaluation method applied
- Grounding Score
- Retrieval Recall
- Hallucination Reduction


## Evaluation Rubic covered
- Document Processing — 25 points
- Retrieval and Grounding — 25 points
- Draft Quality — 10 points
- Code Quality and System Design — 10 points
- Documentation and Clarity — 5 points
Skipped Improvement from Edits