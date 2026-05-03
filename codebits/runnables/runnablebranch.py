# used fr conditional chains 

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda, RunnablePassthrough




load_dotenv()
model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=800, 
    temperature=0.7
    )

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Write a detailed report about {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate( 
    template="Now, summarize this report {text} in simple words in 50 words",
    input_variables=['text']
)

chain=RunnableSequence(prompt1, model, parser)

branch_chain=RunnableBranch(
            (lambda x: len(x.split())> 200 , RunnableSequence(prompt2 | model | parser )),
            RunnablePassthrough()

)
final_chain= RunnableSequence( chain , branch_chain)

result=final_chain.invoke({'topic': "Russian womans vs Indian womans"})
print(result)
final_chain.get_graph().print_ascii()