from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

# Extract Data from PDF file

def load_pdf_file(data):
    loader = DirectoryLoader(data,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    
    documents = loader.load()

    return documents

# Split the Data into Text Chunks

def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks 

# Downoad the Embeddings from HuggingFace

def download_google_generative_ai_embeddings(api_key=None, model_name="models/embedding-001", task_type="retrieval_query"):
    
    if api_key is None:
        api_key = os.environ.get("GEMINI_API_KEY")
        if api_key is None:
            raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it or pass it as an argument.")


    embeddings = GoogleGenerativeAIEmbeddings(model=model_name, google_api_key=api_key, task_type=task_type)
    return embeddings
