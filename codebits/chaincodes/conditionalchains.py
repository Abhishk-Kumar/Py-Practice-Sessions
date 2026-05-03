from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal



load_dotenv()
model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=800, 
    temperature=0.7
    )

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['Positive', 'Negative']=Field(description="The sentiment of the feedback, either Positive or Negative")

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="Find the sentiment of the following review and classify it as positive, negative or neutral: {feedback}, \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

prompt2=PromptTemplate(
    template="Give suitable response to this positive sentiment : {feedback}",
    input_variables=['feedback']
 
)
prompt3=PromptTemplate(
    template="Give suitable response to this negative sentiment : {feedback}",
    input_variables=['feedback'],

)
classifier_chain= prompt1 | model | parser2
branch_chain=RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "Negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Couldn't determine this sentiment")
)

final_chain= classifier_chain | branch_chain
result=final_chain.invoke({'feedback': "I really enjoyed the product, it exceeded my expectations!"})
print(result)

final_chain.get_graph().print_ascii()