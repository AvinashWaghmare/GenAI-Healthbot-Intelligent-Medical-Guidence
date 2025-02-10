from flask import Flask, render_template, jsonify, request
from src.load_data_into_text_chunks import download_google_generative_ai_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

embeddings_model = download_google_generative_ai_embeddings()

index_name = "healthcarebot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings_model,
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

model = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.4)

prompt = ChatPromptTemplate.from_messages(system_prompt)

question_answer_chain = create_stuff_documents_chain(model, prompt)

rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template('chat_index.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        msg = request.form["msg"]
        input = msg
        print(input)
        response = rag_chain.invoke({"input": msg})
        print("Response : ", response["answer"])
        return str(response["answer"])
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
