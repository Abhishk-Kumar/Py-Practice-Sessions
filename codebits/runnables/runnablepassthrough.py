# runnablepassthrough gives output ..same as input no process no change
# it is useful ..like in sequential chain prompt- model-joke -model - explaination...
# here we get explaination only so what we do is we take joke from parser and then send joketo 
# another chain for making explaination and also send joke to runnablepassthrough to print joke also so we got both this way 

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough



load_dotenv()
model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=800, 
    temperature=0.7
    )

parser=StrOutputParser()


# print(passthrough.invoke(23))
# print(passthrough.invoke({"g":"Hello World"}))

prompt1=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate( 
    template="Now, explain this joke  {joke} in simple words",
    input_variables=['joke']
)

joke_generator_chain= RunnableSequence(prompt1, model, parser)

parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination': RunnableSequence(prompt2, model, parser)
})

final_chain=RunnableSequence(joke_generator_chain, parallel_chain)
result=final_chain.invoke({'topic':'coding'})
print(result)
final_chain.get_graph().print_ascii()