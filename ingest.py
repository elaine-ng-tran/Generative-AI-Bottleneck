import os
import json
import math
from sentence_transformers import SentenceTransformer

DOCS_PATH = "./docs"
DB_PATH = "./pure_python_db.json"

def main():
    print("Loading documents from /docs ...")
    if not os.path.exists(DOCS_PATH):
        os.makedirs(DOCS_PATH)
        print(f"Created missing directory: {DOCS_PATH}. Add some .txt files and try again.")
        return

    documents = []
    for root, _, files in os.walk(DOCS_PATH):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    documents.append(f.read())

    if not documents:
        print("No .txt files found in /docs. Add some and try again.")
        return

    print(f"Loaded {len(documents)} document(s).")
    
    # Simple chunking
    chunks = []
    for doc in documents:
        words = doc.split()
        for i in range(0, len(words), 50):
            chunk = " ".join(words[i:i+60])
            chunks.append(chunk)
            
    print(f"Split into {len(chunks)} chunks.")
    print("Embedding locally using SentenceTransformer (all-MiniLM-L6-v2) ...")
    
    try:
        # MiniLM is super small, fast, and runs locally on your Mac CPU instantly
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode(chunks).tolist()
        
        vector_db = []
        for i, emb in enumerate(embeddings):
            vector_db.append({
                "chunk": chunks[i],
                "embedding": emb
            })
            
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(vector_db, f)
            
        print(f"Done! Local vector database saved to {DB_PATH}")
        
    except Exception as e:
        print(f"Local Embedding Error: {e}")

if __name__ == "__main__":
    main()
