from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()
model=ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("api_key"), max_tokens=500, temperature=0.7)

class Person(BaseModel):

    name: str =Field(description= "Name of artist")
    age: int =Field(gt=18, lt=50, description="age of artist")
    city:str =Field(description="place of artist")

parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template='Give me name , age and city of any fictional {place} artist, \n {format_instruction}',
    input_variables=["place"],
    partial_variables={'format_instruction': parser.get_format_instructions()}

)

prompt=template.invoke({'place': "Kanpur"})
print(prompt)
result=model.invoke(prompt)
final_res=parser.parse(result.content)
print(final_res)