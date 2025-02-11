# GenAI-Healthbot-Intelligent-Medical-Guidence

### Overview
```bash
This project is AI-powered Medical Chatbot designed to provide users with accessible health disease information and guidance.
The chatbot utilizes Google's Gemini 1.5 Flash model for natural language generation. 
Google Generative AI Embeddings (embedding-001):Generates vector embeddings of text for semantic understanding and similarity search.
Model Selection: embedding-001.
Embedding Process: Detailed explanation of how text is preprocessed, tokenized, and embedded.
API Integration: How Langchain interacts with the Google Generative AI Embeddings API.
Google Generative AI Embeddings (embedding-001) for semantic understanding, Langchain for the AI pipeline.
Pinecone Vector Database: Stores and efficiently retrieves medical knowledge based on vector embeddings.
Data Source: medical textbooks, research papers, clinical guidelines, reputable health websites.
LangChain: Is a framework for developing applications powered by large language models (LLMs).
Google Gemini 1.5 Flash Model: Generates natural language responses based on the user's query and retrieved information.
Model Selection: Gemini 1.5 Flash (e.g., speed, cost-effectiveness, performance on medical text).
Prompt Engineering: Strategies for crafting effective prompts to guide the model's response generation.
API Integration: How Langchain interacts with the Gemini 1.5 Flash API.
To assist users in understanding medical concepts and terminology.
```
# How to run?
### STEPS:

Create the New repository

```bash
Project repo: https://github.com/AvinashWaghmare/
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n healthbot python=3.10 -y
```

```bash
conda activate healthbot
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 03- Create a .env file in the root directory and add your Pinecone credentials and Gemini API key as follows:
```bash
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GEMINI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
### STEP 04- Download the gemini-1.5-fash model and langchain-google-genai model 

### STEP 05- Download GoogleGenerativeAIEmbeddings model Embedding-001 

### STEP 06- Create a following python files
```bash 
load_data_into_text_chunk.py
prompt.py
store_index.py
app.py
chat_index.html
style.css
```
### STEP 07- Run the following command
```bash
python store_index.py
```
### STEP 08- Run the following command
```bash
python app.py
```
## Open the localhost and run your HEALTHMEDBOT webapp

### Techstack Used
```bash
Python
Google GenAI
Langchain
Flask
Pinecone
Gemini LLM
```