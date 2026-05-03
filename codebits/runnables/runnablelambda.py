# converts simple py func into runnable 


from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda



def wordcount(text):
    return len(text.split())
# runnable_word_counter=RunnableLambda(wordcount)
# res=runnable_word_counter.invoke("Hello World from Groq") # it will return 5 because there are 5 words in this sentence
# print(res)
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


joke_generator_chain=RunnableSequence(prompt1, model, parser)

parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),
    'wordcount':RunnableLambda(wordcount),
})
# parallel_chain=RunnableParallel({
#     'joke': RunnablePassthrough(),
#     'wordcount':RunnableLambda(lambda x:len(x.split())),
# })

final_chain=RunnableSequence(joke_generator_chain, parallel_chain)

result=final_chain.invoke({'topic':'coding'})
print(result)
final_chain.get_graph().print_ascii()   