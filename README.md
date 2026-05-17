# Generative AI Bottleneck
<img width="788" height="73" alt="Screen Shot 2026-05-10 at 11 24 02 AM" src="https://github.com/user-attachments/assets/512112a8-1722-4224-957d-1aaa3b4ec9a8" />

# Why RAG and LLM Hallucination Exists
LLM such as ChatGPT, Google Gemini and Claude (Anthropic) have training cutoff. These models often confidently state outdated and (sometimes) made up information. For example, in this prompt, the user asks ChatGPT if Heeseung has left ENHYPEN and confidently answers no while credible sources stated his departure of the group March 10, 2026. With the recent surge of ChatGPT usage, doubling since 2023, this project aims to fix grounding of LLM response to keep up to date with very recent source documents before generating a concrete factual answer. 

# How This Works 
When user asks question, Langchain pulls relevent chunks from document store and retrieve cotext from LLM prompt. Rather than have LLM gather information from training, it is given source documents to answer from, ensuring answers are backed up with concrete evidence. 

# Stack/Tools 
Langchain | OpenAI API | Chroma DB | Python | Bash | GIT | GITHUB 

# Input/Output 
<img width="1339" height="102" alt="Screen Shot 2026-05-17 at 4 33 36 PM" src="https://github.com/user-attachments/assets/ea0293a4-af07-49ba-93c7-74f85a589516" />
<img width="1337" height="103" alt="Screen Shot 2026-05-17 at 4 34 13 PM" src="https://github.com/user-attachments/assets/4db60f36-66b8-40a9-9ab6-ff826f788d55" />
<img width="1089" height="555" alt="Screen Shot 2026-05-17 at 4 35 14 PM" src="https://github.com/user-attachments/assets/0387d213-ae82-40f0-88cb-4aa66802179e" />


