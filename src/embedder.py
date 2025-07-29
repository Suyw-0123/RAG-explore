# src/embedder.py

from sklearn.feature_extraction.text import TfidfVectorizer

class Embedder:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.docs = []
        self.vectors = None

    def add_documents(self, docs: list[str]):
        self.docs = docs
        self.vectors = self.vectorizer.fit_transform(docs)

    def get_relevant_docs(self, query: str, top_k: int = 1):
        query_vec = self.vectorizer.transform([query])
        scores = (self.vectors * query_vec.T).toarray()
        top_indices = scores[:, 0].argsort()[::-1][:top_k]
        return [self.docs[i] for i in top_indices]
