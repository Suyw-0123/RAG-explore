# src/rag_pipeline.py

import os
import google.generativeai as genai
from dotenv import load_dotenv
from retriever import get_top_documents

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def run_rag_pipeline(query: str):
    context = get_top_documents(query, k=2)
    context_text = "\n".join(context)

    prompt = f"""
根據下列背景文件回答問題：
{context_text}

問題：{query}
請用清楚、專業的語氣簡單解釋。
"""

    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    query = input("請輸入問題：")
    answer = run_rag_pipeline(query)
    print("\n回答：", answer)
