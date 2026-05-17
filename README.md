# Generative AI Bottleneck
<img width="788" height="73" alt="Screen Shot 2026-05-10 at 11 24 02 AM" src="https://github.com/user-attachments/assets/512112a8-1722-4224-957d-1aaa3b4ec9a8" />

# Why RAG and LLM Hallucination Exists
LLM such as ChatGPT, Google Gemini and Claude (Anthropic) have training cutoff. These models often confidently state outdated and (sometimes) made up information. For example, in this prompt, the user asks ChatGPT if Heeseung has left ENHYPEN and confidently answers no while credible sources stated his departure of the group March 10, 2026. With the recent surge of ChatGPT usage, doubling since 2023, this project aims to fix grounding of LLM response to keep up to date with very recent source documents before generating a concrete factual answer. 

# How This Works 
When user asks question, Langchain pulls relevent chunks from document store and retrieve cotext from LLM prompt. Rather than have LLM gather information from training, it is given source documents to answer from, ensuring answers are backed up with concrete evidence. 

# Stack/Tools 
Langchain | OpenAI API | Chroma DB | Python | Bash | GIT | GITHUB 
-
DEVICE: MacBook Air Monterey and up | LLM: ChatGPT | TOTAL COST: $5

# How to Train the LLM 
STEP 1: Ensure you have Python installed (preferably latest version, this project I used 3.14.5). 
-
STEP 2: If you have no API credits, you can load around $5 (system will give ERROR later if no available tokens)
-
STEP 3 (Create your TextEdit documents): 
Create an API key from your LLM of choice (I used ChatGPT-4o mini). 
-
Make sure you copy your API Key onto TextEdit (command + search: "TextEdit"). Click FORMAT at top left cornder to convert to PlainText. 
Write Text: OPEN_AI_KEY=[*INSERT API KEY*] -- and save as ".env" file.
-
Make another TextEdit document for your installation tools, also convert to PlainText. 
Write Text: 
langchain 
langchain-openai 
lanchain-community 
chromadb
openai 
python-dotenv
-- and save as "requirements.txt" 
-
STEP 6: Open your terminal (you will be using this for majority of this project). BTW, you should preferably only have a README on your GITHUB repository, most of this will be creating your own files from terminal HEHE. 
- 
STEP 7: Clone your GITHUB Repo. 
Use Terminal Command: git clone https://github.com/*YOUR GITHUB NAME*/*YOUR PROJECT NAME*
- 
