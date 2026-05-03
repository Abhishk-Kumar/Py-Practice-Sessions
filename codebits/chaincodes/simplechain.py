from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser



load_dotenv()
model=ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("api_key"), max_tokens=500, temperature=0.7)

parser=StrOutputParser()
prompt=PromptTemplate(
    template=" Write 5 pointer details about {topic}, \n ",
    input_variables=['topic']
  
)

chain= prompt | model | parser
result= chain.invoke({'topic' : "Cricket"})
print(result)