from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = GoogleGenerativeAI(
    google_api_key=os.environ["GOOGLE_API_KEY"],
    temperature=0,
    model="gemini-1.5-pro-latest"
)

instructor_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb_file_path = "faiss_index"

def create_vector_db():
    loader = CSVLoader(file_path="codebasics_faqs.csv", source_column='prompt')
    data = loader.load()
    vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever()

    prompt_template = """Given the following context and a question, generate a conversational, helpful, and detailed answer based on this context only.
    Present the information in a natural, flowing way that addresses all parts of the question thoroughly.
    Include all relevant details from the "response" section in the context to provide a complete answer.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}

    Your response should be detailed and helpful, providing all available information in a conversational tone:"""

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=['context', 'question']
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )

    return chain


if __name__ == "__main__":
    # create_vector_db()

    chain = get_qa_chain()

    print(chain("Do you provide internships? Do you have EMI options?"))
    

