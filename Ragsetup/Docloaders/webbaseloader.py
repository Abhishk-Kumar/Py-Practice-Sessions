from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=800, 
    temperature=0.7
    )
url='https://en.wikipedia.org/wiki/Mahatma_Gandhi'
loader=WebBaseLoader(url)
parser=StrOutputParser()

docs=loader.load()
print(docs[0].page_content)