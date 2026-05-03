# 4 type of parser strouparser, jsonoutputparser, pydanticparser, structureparser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model=ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("api_key"), max_tokens=500, temperature=0.7)

template1=PromptTemplate(
    template="Write detailed report about {topic}",
    input_variables=["topic"]
)

template2=PromptTemplate(
    template="Write 5 line summary about {text}",
    input_variables=["text"]

)
parser=StrOutputParser()

chain= template1 | model |  parser | template2 | model | parser 

result=chain.invoke({'topic' : "Black Hole"})

print(result)
