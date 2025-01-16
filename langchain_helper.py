from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

#important note sentence-transformers==2.2.2, huggingface_hub==0.25.0

load_dotenv()

#loading google gemini ai with api_key, setting temperature to 0.1 for least creativity 
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",google_api_key=os.environ["GEMINI_API_KEY"], temperature=0.1)

#using instructor embedding and default model
instructor_embeddings = HuggingFaceInstructEmbeddings(
    model_name = "hkunlp/instructor-base",
    model_kwargs = {'device': 'cpu'}
)

vectordb_file_path = "faiss_index"
def create_vector_db():
    #load the csv file using CSVLoader
    loader = CSVLoader(file_path="faqs.csv", 
                   csv_args={
                    "delimiter": ",",
                    "quotechar": '"',
                    "fieldnames": ["prompt", "response"]
    },source_column="prompt")
    docs = loader.load()
    #storing vectordb using FAISS
    vector_db = FAISS.from_documents(documents = docs, embedding = instructor_embeddings)
    vector_db.save_local(vectordb_file_path)

def get_qa_chain():
    #load the vectordb using load_local
    vectordb = FAISS.load_local(vectordb_file_path,instructor_embeddings,allow_dangerous_deserialization=True)

    #create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold = 0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template = prompt_template, input_variables = ['context', 'question'])

    chain_type_kwargs = {"prompt": PROMPT}

    chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type = "stuff",
        retriever = retriever,
        input_key = "query",
        return_source_documents = True,
        chain_type_kwargs=chain_type_kwargs
    )

    return chain

if __name__ == "__main__":
    create_vector_db()
    chain = get_qa_chain()
    print(chain("Do you have monthly payments?"))