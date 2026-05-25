from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field


load_dotenv()
model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=800, 
    temperature=0.7
    )

# class ResumeAnalysis(BaseModel):
#     key_skills:str=Field(description="Key skills mentioned in the resume"),
#     experience_summary:str=Field(description="Summary of the candidate's work experience"),
#     fir_score=int=Field(description="Fitment score indicating how well the resume matches the job description, on a scale of 0 to 100"),
#     gaps=str=Field(description="Any noticeable gaps in the candidate's employment history"),
#     suggestions:str=Field(description="Suggestions for improving the resume to better match the job description")

# READ Resume
with open('resume.txt', "r" ,encoding='utf-8') as f:
    resume=f.read()
# READ PROMPT 
with open('resume_prompt.txt', "r" ,encoding='utf-8') as f:
    resume_prompt=f.read()

prompt=PromptTemplate.from_template(resume_prompt)

finalprompt=prompt.invoke({'resume':resume})


print(finalprompt.text)