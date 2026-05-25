from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence




load_dotenv()
model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=800, 
    temperature=0.7
    )

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate( 
    template="Now, explain this joke  {joke} in simple words",
    input_variables=['joke']
)

chain=RunnableSequence(prompt1, model, parser, prompt2, model, parser)
# chain=RunnableSequence(prompt | model |parser | prompt2 | model |parser) 

result=chain.invoke({'topic': "programming"})

print(result)
chain.get_graph().print_ascii()