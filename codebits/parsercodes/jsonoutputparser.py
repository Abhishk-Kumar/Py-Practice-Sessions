from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

import os
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()
model=ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("api_key"), max_tokens=500, temperature=0.7)

parser=JsonOutputParser()

template=PromptTemplate(
    template=" Give me name, age and city of a fictional person , \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction' : parser.get_format_instructions()}

)

# prompt=template.format()
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)

chain= template | model | parser

final_result=chain.invoke({})

print(final_result)
print(type(final_result))
print(final_result['name'])

#json output parser doesnt enforce any schema ...so it has flaw so we will use structured output parser for this₹