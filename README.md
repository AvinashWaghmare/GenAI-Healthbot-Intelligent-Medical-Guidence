# GenAI-Healthbot-Intelligent-Medical-Guidence

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