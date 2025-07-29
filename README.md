
# RAG-explore

探索 Retrieval-Augmented Generation（RAG）技術的 Python 實驗平台，結合 LLM（如 Gemini）與向量資料庫（FAISS、ChromaDB），支援自訂文本檢索、嵌入、問答與分析。

---

## 🚀 功能特色

- 支援自訂文本（如 data/sample_docs.txt）作為知識庫
- 以 SentenceTransformers 產生語意嵌入
- 向量檢索採用 FAISS，快速取得最相關段落
- 整合 Google Gemini API，實現 RAG 問答
- 可用 Jupyter Notebook 進行流程分析與實驗

---

## 📁 專案結構

- src/        主程式（retriever, embedder, rag_pipeline 等）
- data/       存放原始或處理過的資料（如 sample_docs.txt）
- notebook/   Jupyter Notebook 實驗與流程分析

---

## 📦 安裝方式

建議使用 conda 或 venv 建立虛擬環境：

```bash
conda create -n rag-env python=3.10
conda activate rag-env
pip install -r requirements.txt
```

如需 Google Gemini API，請申請 API 金鑰並於 .env 檔案設定：
```
GOOGLE_API_KEY=你的金鑰
```

---

## 🛠️ 使用教學

1. 將你的知識文本放入 data/sample_docs.txt（可用空行分段）
2. 執行主程式：
   ```bash
   python src/rag_pipeline.py
   ```
3. 輸入問題，系統會自動檢索最相關段落並用 Gemini 回答

---

## 🔍 技術細節

- 文本分段：以空行分割，提升語意檢索精度
- 嵌入模型：預設 all-MiniLM-L6-v2（可自訂）
- 向量庫：FAISS，支援高效相似度搜尋
- RAG Pipeline：檢索 top-k 段落，組合 context，送入 LLM 生成答案

---

## 📊 Notebook 實驗

可於 notebook/ 目錄建立 Jupyter Notebook，分析嵌入、檢索、問答流程與效果。

---

## 📝 範例

```python
from retriever import get_top_documents
query = "他們是如何打敗暗影霸王龍的？"
docs = get_top_documents(query, k=5)
print("檢索到的段落：", docs)
```

---

## 🤝 貢獻方式

歡迎 PR、issue 討論新功能、bug 或技術交流。

---

## 📄 License

MIT

