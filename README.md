# Generative AI Bottleneck
<img width="788" height="73" alt="Screen Shot 2026-05-10 at 11 24 02 AM" src="https://github.com/user-attachments/assets/512112a8-1722-4224-957d-1aaa3b4ec9a8" />

# Why RAG and LLM Hallucination Exists
LLM such as ChatGPT, Google Gemini and Claude (Anthropic) have training cutoff. These models often confidently state outdated and (sometimes) made up information. For example, in this prompt, the user asks ChatGPT if Heeseung has left ENHYPEN and confidently answers no while credible sources stated his departure of the group March 10, 2026. With the recent surge of ChatGPT usage, doubling since 2023, this project aims to fix grounding of LLM response to keep up to date with very recent source documents before generating a concrete factual answer. 

# How This Works 
User question -> Langchain to pull relevent chunks from document store -> Retrieved context via LLM prompt -> Grounded answer 

Rather than have LLM gather information from training, it is given source documents to answer from. 

# STACK
Langchain |
OpenAI API |
Chroma DB |
Python |
Bash |
GIT 
