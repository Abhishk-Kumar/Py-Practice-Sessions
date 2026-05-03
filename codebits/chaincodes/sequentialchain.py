from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser



load_dotenv()
model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=500, 
    temperature=0.7
    )

parser=StrOutputParser()
prompt1=PromptTemplate(
    template=" Write detailed report about {topic}, \n ",
    input_variables=['topic']
  
)

prompt2=PromptTemplate(
    template=" Write 5 pointer summary about {text}, \n ",
    input_variables=['text']
  
)

chain= prompt1 | model | parser | prompt2 | model | parser
result=chain.invoke({"topic": "Sex"})

print(result)

chain.get_graph().print_ascii()