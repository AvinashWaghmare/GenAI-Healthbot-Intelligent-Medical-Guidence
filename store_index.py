from src.load_data_into_text_chunks import load_pdf_file, text_split, download_google_generative_ai_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from pinecone.exceptions import PineconeException
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data = load_pdf_file(data='D:\Work\GenAI-Healthbot-Intelligent-Medical-Guidence\Data')
text_chunks = text_split(extracted_data)
embeddings_model= download_google_generative_ai_embeddings()
print(embeddings_model)
print("GoogleGenerativeAIEmbeddings loaded successfully!")

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "healthcarebot"

try:
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    print(f"Index '{index_name}' created successfully.")

except PineconeException as e:
    if "already exists" in str(e).lower():  # Check if the exception is about existing index
        print(f"Index '{index_name}' already exists. Skipping creation.")
    else:  # Re-raise the exception if it's something else
        print(f"An error occurred during index creation: {e}")
        
        raise  # Re-raise the exception to stop program.
except Exception as e: # Catch other potential exceptions
    print(f"An unexpected error occurred: {e}")
    raise # Re-raise the exception to stop program.

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings_model,
)