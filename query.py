import os
import json
import math
import sys
from dotenv import load_dotenv
from openai import OpenAI
from sentence_transformers import SentenceTransformer

load_dotenv()

DB_PATH = "./pure_python_db.json"

def cosine_similarity(v1, v2):
    dot_product = sum(x * y for x, y in zip(v1, v2))
    magnitude1 = math.sqrt(sum(x * x for x in v1))
    magnitude2 = math.sqrt(sum(x * x for x in v2))
    if not magnitude1 or not magnitude2:
        return 0
    return dot_product / (magnitude1 * magnitude2)

def main():
    if len(sys.argv) < 2:
        query_text = "Has Heeseung left ENHYPEN?"
    else:
        query_text = sys.argv[1]

    if not os.path.exists(DB_PATH):
        print(f"Error: Database file {DB_PATH} not found. Run ingest.py first.")
        return

    with open(DB_PATH, 'r', encoding='utf-8') as f:
        vector_db = json.load(f)

    # 1. Embed the user's question locally using the exact same model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode(query_text).tolist()

    # 2. Find the most contextually relevant chunk using math
    best_chunk = None
    highest_similarity = -1

    for item in vector_db:
        similarity = cosine_similarity(query_embedding, item["embedding"])
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_chunk = item["chunk"]

    # 3. Use standard OpenAI chat to answer using your injected truth
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file.")
        return
        
    client = OpenAI(api_key=api_key)
    
    # We build the absolute ironclad prompt context here
    prompt = f"""You are a precise assistant. Answer the user's question using ONLY the provided context below. If the context doesn't mention the answer, rely on the context stating facts as of 2026.

Context:
{best_chunk}

User Question: {query_text}
Answer:"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        print("\n=== RAG SEARCH RESULT ===")
        print(f"Retrieved Context: {best_chunk}")
        print("=========================\n")
        print("=== AI RESPONSE ===")
        print(response.choices[0].message.content)
        print("===================")
        
    except Exception as e:
        print(f"OpenAI API Error: {e}")

if __name__ == "__main__":
    main()
