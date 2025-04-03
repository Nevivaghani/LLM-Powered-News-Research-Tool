# import main
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.chains import RetrievalQA 
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI # import the new GoogleGenerativeAI class
# from langchain_community.llms import GooglePalm
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize GoogleGenerativeAI LLM
llm = GoogleGenerativeAI(google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.7,  model="gemini-1.5-pro-latest")

loader = CSVLoader(file_path = "codebasics_faqs.csv", source_column = 'prompt' )
data = loader.load()

instructor_embeddings = HuggingFaceInstructEmbeddings(
    # query_instruction = "Represent the query for retrieval: "
)

# e = embeddings.embed_query("what is your refund policy?")
# print(e)
# print(len(e))

vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)

retriever = vectordb.as_retriever()
rdocs = retriever.get_relevant_documents("for how long is this code valid?")
# print(rdocs)

prompt_template = """Given the following context and a question, generate an answer based on this context only.
In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

CONTEXT: {context}

QUESTION: {question}"""

PROMPT = PromptTemplate(
    template = prompt_template, 
    input_variables = ['context', 'question']
)

chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",  # Required in newer versions
    return_source_documents=True,
    chain_type_kwargs = {"prompt" : PROMPT}
)

ch = chain("DO you have javascript course?")
print(ch)