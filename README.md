# Domad AI: GCP-First RAG Delivery Starter Kit

Welcome to the **open-core delivery toolkit** from Domad AI — your launchpad for building production-grade Retrieval-Augmented Generation (RAG) systems, starting with Google Cloud Platform.

This toolkit is designed to give developers and AI teams a battle-tested, modular RAG backend that is:
- **Fast to deploy locally or on GCP**
- **Extensible for enterprise scenarios**
- **Cleanly separated into public + commercial capabilities**

---

## 💡 What This Toolkit Does

This starter kit enables:
- Asking questions in natural language
- Retrieving answers grounded in your document data
- Running locally for fast prototyping or deploying on GCP Cloud Run
- The ability to evolve into an agent-based API orchestration assistant

**This public version includes the core RAG flow** using LangChain + FAISS or Chroma with FastAPI.

---

## 📦 Toolkit Structure

```
starter-rag-gcp/
├── core-lite/            # Public core: retrieval + prompt logic
│   ├── chain.py
│   ├── vectorstore.py
│   └── config.py
├── app/                  # FastAPI app exposing /query
│   └── main.py
├── deploy/               # GCP / Docker deployment configs
│   ├── gcp/
│   └── docker/
├── data/                 # Sample data to index
│   └── sample.txt
├── requirements.txt
├── .env.example
├── README.md
```

---

## 🚀 Quickstart: Local Hello World

### 1. Setup

```bash
git clone https://github.com/your-org/starter-rag-gcp.git
cd starter-rag-gcp
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Ingest Sample Data

```bash
# data/sample.txt contains your demo knowledge base
# Make sure vectorstore indexes it using FAISS or Chroma
```

### 3. Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

### 4. Query it

```bash
curl -X POST http://localhost:8000/query \
     -H "Content-Type: application/json" \
     -d '{"question": "What is Domad AI?"}'
```

Expected output:
```json
{
  "answer": "Domad AI helps businesses rapidly deploy GenAI solutions..."
}
```

---

## ☁️ GCP Deployment (Cloud Run)

### 1. Prerequisites
- A GCP project with Cloud Run, Firestore, and Storage enabled
- `gcloud` CLI installed and authenticated

### 2. Deploy to Cloud Run

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/rag-api
gcloud run deploy rag-api \
  --image gcr.io/YOUR_PROJECT_ID/rag-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### 3. Hit the public endpoint

```bash
curl -X POST https://your-cloud-run-url/query \
     -H "Content-Type: application/json" \
     -d '{"question": "What is Domad AI?"}'
```

---

## 🔒 What's in the Pro Version?

The public version is lightweight and powerful, but we reserve advanced features for the licensed toolkit:

- 🧠 Query rewriting for better recall
- 🔎 Summary + metadata-based indexing
- 🏗️ Reranker (BGE, ColBERT)
- 🔗 OpenAPI-aware agent integration
- 🧭 Prompt selectors and verifier chains
- 🧠 Memory and multi-turn flows
- ☁️ Hosted monitoring, eval, and scaling

Contact [https://domad-ai.com](https://domad-ai.com) to access the full delivery framework.

---

## 📝 License

This project is licensed under the [Business Source License](https://mariadb.com/bsl11) (or MIT if chosen).  
Use is allowed for research, experimentation, and evaluation. For commercial deployment or advanced usage, please contact Domad AI.

---

_This is a Domad AI open delivery starter kit._  
