from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()
model=ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("api_key"), max_tokens=500, temperature=0.7)

schema=[
    ResponseSchema(name="fact1 :", description="Description about fact1 "),
    ResponseSchema(name="fact2 ", description="Description about fact2 "),
    ResponseSchema(name="fact3 :", description="Description about fact3 ")
]
parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="write 3 facts about any {topic}, \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt=template.invoke("Amazon forest")

# prompt=template.invoke({'topic': "Amazon forest"})
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)
# print(final_result)

chain = template | model | parser

result=chain.invoke({'topic' : "AMAZON forest"})
print(result)

#now flaw with this parser is we cant do data validation here so we use pydantic parser
