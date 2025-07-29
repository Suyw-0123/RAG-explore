# src/rag_pipeline.py

import os
import google.generativeai as genai
from dotenv import load_dotenv
from retriever import get_top_documents
from transformers import AutoTokenizer

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def run_rag_pipeline(query: str):
    context = get_top_documents(query, k=8)
    context_text = "\n".join(context)
    # 計算 token 數量 (Debug用)
    '''tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
    token_count = len(tokenizer(context_text)["input_ids"])
    print(f"DEBUG: context_text token數 = {token_count}")
    print("DEBUG: context_text內容 =\n", context_text)
    print("\n")
    '''

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
