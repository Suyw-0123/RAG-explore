# RAG-explore

本專案是探索 Retrieval-Augmented Generation（RAG）的實驗平台，預計整合 LLM 與向量搜尋技術。

## 📁 專案結構

src/ # 程式主體（retriever, embedder, pipeline 等）
data/ # 存放原始或處理過的資料
notebook/ # Jupyter Notebook 實驗與測試


## 📦 安裝方式

```bash
# 建立虛擬環境（可使用 conda 或 venv）
pip install -r requirements.txt


---

### 📄 `src/rag_pipeline.py`（空白模板）

```python
# src/rag_pipeline.py

def run_rag_pipeline(query: str):
    # TODO: 撰寫完整的 RAG pipeline
    return "這是模擬回覆：您查詢的是 " + query


if __name__ == "__main__":
    response = run_rag_pipeline("什麼是向量資料庫？")
    print(response)
