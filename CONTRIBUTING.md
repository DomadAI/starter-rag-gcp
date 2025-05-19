# 🛠️ Contributing to Domad AI RAG Starter Kit

Thanks for your interest in contributing to this open-core toolkit!

This project follows a clean and secure development workflow. Please read the steps below to contribute effectively.

---

## 🚫 No Direct Branch Creation

To maintain repo quality and security:
- ✅ Direct branch creation on this repo is **disabled**
- ✅ Only core maintainers can push or create branches
- ✅ Contributors must work via **forks + pull requests**

---

## ✅ Contribution Workflow

1. **Fork** this repository to your own GitHub account.
2. Create a feature branch on your fork (e.g. `feature/my-improvement`)
3. Make and test your changes locally.
4. Submit a **pull request to `main`** in this repo.
5. Wait for review and feedback from a maintainer.

---

## 📦 Install + Run Locally

```bash
git clone https://github.com/domadai/starter-rag-gcp.git
cd starter-rag-gcp
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 💬 Questions?

Open an issue or [contact the team at Domad AI](https://domad-ai.com).

Thanks for contributing!
