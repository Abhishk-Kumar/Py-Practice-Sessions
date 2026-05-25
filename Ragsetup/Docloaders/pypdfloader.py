# it uses pypdf library under hood not good much with scanned pdf or click photo pdfs
# each page here of pdf is document object

from langchain_community.document_loaders import PyPDFLoader
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

loader=PyPDFLoader('CN_Unit3_AKTU_Summary.pdf')
parser=StrOutputParser()

docs=loader.load()

# load func as well as lazy_load func are there in pypdfloader, load func loads all the pages at once and lazy_load func loads one page at a time and returns an iterator
#  it print each entry of doc and delete from memory 
print(docs[0].page_content)
print(docs[1].metadata)

# directory loader 3 4 books 
# webbase loader //text from web pages 