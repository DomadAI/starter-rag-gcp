# 🚀 Domad AI: Open RAG Delivery Starter Kit

This project is designed to run locally and on Docker, with upcoming support for full GCP deployment in the Pro edition.

Welcome to the **open-core RAG toolkit** from Domad AI — a GenAI-first engineering company that builds modern delivery kits for Retrieval-Augmented Generation (RAG), AI-SDLC, and platform modernization.

This starter project demonstrates how to build a domain-safe GenAI assistant that only responds to questions grounded in your organization's data.

---

## 📦 What This Starter Kit Includes

- ✅ LangChain v0.2+ architecture using `langchain_community`
- ✅ FAISS-based vector index with prebuilt content
- ✅ Modular prompt engine with strict/verbose/default styles
- ✅ FastAPI API endpoint for querying
- ✅ `.env`-driven configuration for flexible deployment
- ✅ Docker support for quick testing or deployment

---

## 🧠 What It Can Do (Out of the Box)

- Answer questions **only about Domad AI**
- Enforce **strict fallback mode** for unknown queries
- Let you swap between prompt tones like:
  - `strict`: professional + brand-safe
  - `verbose`: informative + friendly
  - `default`: neutral baseline

---

## 🔧 How to Use Locally

### 1. Clone & Install

```bash
git clone https://github.com/domadai/starter-rag-gcp.git
cd starter-rag-gcp
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure

```bash
cp .env.example .env
```

Then edit `.env` and insert your OpenAI key:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

Optional:
```env
PROMPT_STYLE=strict
STRICT_MODE=true
```

### 3. Build Vectorstore

```bash
python build_vectorstore.py
```

### 4. Start API

```bash
uvicorn app.main:app --reload
```

---

## 🔍 Test the Agent

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Domad AI?"}'
```

❌ Try a non-Domad query in strict mode:

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the capital of France?"}'
```

---

## 🐳 Docker Support

### 🔁 Option A: Run Without Cloning (Prebuilt Image)

You can test this project directly with Docker:

```bash
docker run -p 8000:8000 -e OPENAI_API_KEY=sk-xxx domadai/domad-rag:latest
```

Or pass your `.env` file:

```bash
docker run -p 8000:8000 --env-file .env domadai/domad-rag:latest
```

> Visit [http://localhost:8000](http://localhost:8000)

---

### 🛠️ Option B: Build Your Own Image

```bash
docker build -t domadai/domad-rag:latest .
docker run -p 8000:8000 --env-file .env domadai/domad-rag:latest
```

---

## 🛠️ Coming in the Pro Version

- 🔗 OpenAPI-aware agent routing
- 🧠 Local LLMs (Mistral, Mixtral)
- 📊 Logging + conversation memory
- 🛡️ Brand-safe inference & reranking
- ☁️ Cloud-native GCP Firestore & GCS support

---

## 📜 License

This project is released under the Business Source License (BSL 1.1).  
For commercial use or advanced features, [contact Domad AI](https://domad-ai.com).

---

_This is a Domad AI open delivery starter kit._
