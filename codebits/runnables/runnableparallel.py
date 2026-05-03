from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence



load_dotenv()
model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=800, 
    temperature=0.7
    )

parser=StrOutputParser()


prompt1=PromptTemplate(
    template=" Generate twitter post about {topic}, \n ",
    input_variables=['topic']
  
)

prompt2=PromptTemplate(
    template=" Generate linkedin post about {topic}, \n  \n",
    input_variables=['topic']
  
)



# 2 parallel chains for generating notes and quests are made here 
parallel_chain=RunnableParallel({
    'tweet':   RunnableSequence(prompt1, model, parser),
    'linkin' : RunnableSequence(prompt2, model, parser)
}
)

result=parallel_chain.invoke({'topic': "AI"})
print(result)

parallel_chain.get_graph().print_ascii()