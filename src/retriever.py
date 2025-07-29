# src/retriever.py

import os
import faiss
from sentence_transformers import SentenceTransformer

def load_docs_from_txt(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    docs = [p.strip() for p in content.split('\n\n') if p.strip()]
    return docs

model_name = "all-MiniLM-L6-v2"
embedder = SentenceTransformer(model_name)

DOC_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_docs.txt")
docs = load_docs_from_txt(DOC_PATH)
doc_embeddings = embedder.encode(docs, convert_to_numpy=True)

index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)

def get_top_documents(query: str, k: int = 5):
    query_emb = embedder.encode([query], convert_to_numpy=True)
    D, I = index.search(query_emb, k)
    return [docs[i] for i in I[0]]
