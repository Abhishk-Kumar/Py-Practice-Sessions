from langchain_community.document_loaders import TextLoader
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

loader=TextLoader('cricket.txt', encoding='utf-8')
parser=StrOutputParser()

docs=loader.load()
# print(docs)
# print(type(docs))
# print(len(docs))
# print(docs[0])
# print(type(docs[0]))

template=PromptTemplate(
    template="Write summary about the poem , \n {poem}",
    input_variables=['poem']
)



print(docs[0].page_content)
print(docs[0].metadata)

chain= template | model | parser

print(chain.invoke({'poem': docs[0].page_content}))