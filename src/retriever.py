# src/retriever.py

from embedder import Embedder

def load_sample_docs():
    return [
        "RAG 是一種結合 LLM 和文件檢索的架構。",
        "Gemini 是 Google 推出的生成式語言模型。",
        "Faiss 可以用來進行高效率的向量相似度搜尋。",
    ]

def get_top_documents(query: str, k: int = 1):
    docs = load_sample_docs()
    embedder = Embedder()
    embedder.add_documents(docs)
    return embedder.get_relevant_docs(query, top_k=k)
