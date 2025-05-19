import os
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA

# Import selected prompt from modular prompt folder
from core_lite.prompts import SELECTED_PROMPT

# Load env vars
load_dotenv()

# Configurable constants
VECTORSTORE_DIR = os.getenv("VECTORSTORE_PATH", "vectorstore")
STRICT_MODE = os.getenv("STRICT_MODE", "true").lower() == "true"
MIN_RESULTS = int(os.getenv("MIN_RESULTS", 1))

def run_chain(question: str) -> str:
    if not os.path.exists(VECTORSTORE_DIR):
        return "❌ Vectorstore not found. Please run build_vectorstore.py first."

    try:
        embeddings = OpenAIEmbeddings()
        # ✅ SAFE: We're loading a vectorstore we created ourselves, not from an untrusted source.
        # This flag is required as of LangChain v0.2+ to allow deserialization of metadata stored in .pkl format.
        db = FAISS.load_local(VECTORSTORE_DIR, embeddings, allow_dangerous_deserialization=True)
    except Exception as e:
        return f"❌ Error loading vectorstore: {e}"

    retriever = db.as_retriever(search_kwargs={"k": 4})
    llm = OpenAI(temperature=0)

    try:
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": SELECTED_PROMPT}
        )

        result = qa({"query": question})

        if not result.get("source_documents") and STRICT_MODE:
            return "I can only answer questions about Domad AI."

        return result["result"].strip()

    except Exception as e:
        return f"❌ Error running QA chain: {e}"
