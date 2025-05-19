import os
import argparse
from dotenv import load_dotenv

try:
    from langchain_community.vectorstores import FAISS
except ImportError:
    print("❌ FAISS import failed. Please run:")
    print("   pip install faiss-cpu   # or faiss-gpu if using CUDA")
    exit(1)

try:
    from langchain_community.embeddings import OpenAIEmbeddings
except ImportError:
    print("❌ OpenAIEmbeddings import failed.")
    print("   pip install -U openai langchain-openai")
    exit(1)

try:
    from langchain_community.document_loaders import TextLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
except ImportError:
    print("❌ Required document loader or text splitter not found.")
    print("   pip install langchain-community")
    exit(1)

def build_vectorstore(data_dir: str, output_dir: str, vectorstore_type: str = "faiss", indexing_mode: str = "chunk"):
    print(f"🔍 Loading source files from: {data_dir}")
    documents = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            loader = TextLoader(os.path.join(data_dir, filename))
            documents.extend(loader.load())

    if not documents:
        print("⚠️ No documents found. Make sure your data directory contains .txt files.")
        exit(1)

    print(f"📚 Loaded {len(documents)} documents")

    # Chunking (can extend later for summary/hybrid indexing)
    if indexing_mode == "chunk":
        print(f"🧠 Using chunk-based indexing (default)")
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks = splitter.split_documents(documents)
    else:
        raise ValueError(f"❌ Unsupported indexing mode: {indexing_mode}")

    print("🔗 Creating OpenAI embeddings...")
    try:
        embeddings = OpenAIEmbeddings()
    except Exception as e:
        print(f"❌ Failed to initialize OpenAIEmbeddings: {e}")
        print("Make sure you have set OPENAI_API_KEY in your .env file.")
        exit(1)

    if vectorstore_type.lower() == "faiss":
        print("💾 Building FAISS vectorstore...")
        try:
            db = FAISS.from_documents(chunks, embeddings)
            db.save_local(output_dir)
        except Exception as e:
            print(f"❌ Failed to build FAISS vectorstore: {e}")
            print("Ensure FAISS is installed: pip install faiss-cpu")
            exit(1)
    else:
        raise ValueError(f"❌ Unsupported vectorstore type: {vectorstore_type}")

    print(f"✅ Vectorstore successfully saved to: {output_dir}")

if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description="Build a vectorstore from .txt files in a directory")
    parser.add_argument("--data_dir", type=str, default="data", help="Directory containing .txt files")
    parser.add_argument("--output_dir", type=str, default="vectorstore", help="Where to save the vectorstore")
    parser.add_argument("--type", type=str, default=os.getenv("VECTORSTORE_TYPE", "faiss"), help="Vectorstore type (e.g., faiss)")
    parser.add_argument("--indexing_mode", type=str, default="chunk", help="Indexing strategy: chunk (default), summary (Pro), hybrid (Pro)")

    args = parser.parse_args()
    build_vectorstore(args.data_dir, args.output_dir, args.type, args.indexing_mode)
