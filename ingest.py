python ingest.py
"""
 
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
 
load_dotenv()  # reads your .env file for OPENAI_API_KEY
 
DOCS_PATH = "./docs"
CHROMA_PATH = "./chroma_db"
 
 
def main():
    print("📂 Loading documents from /docs ...")
    loader = DirectoryLoader(
        DOCS_PATH,
        glob="**/*.txt",
        loader_cls=TextLoader
    )
    documents = loader.load()
 
    if not documents:
        print("No .txt files found in /docs. Add some and try again.")
        return
 
    print(f"Loaded {len(documents)} document(s).")
 
    # Split into smaller chunks so retrieval is precise
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks.")
 
    # Embed and store
    print("🔢 Embedding and storing in ChromaDB ...")
    embeddings = OpenAIEmbeddings()
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    print(f"Done! Vector store saved to {CHROMA_PATH}/")
 
 
if __name__ == "__main__":
    main()
 
