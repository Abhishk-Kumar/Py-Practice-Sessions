from langchain_groq import ChatGroq
from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()
import os

model=ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("api_key"), temperature=0.5)
# template="""
# You are an expert in {domain} with deep knowledge and practical experience.

# Your task is:
# "{task}"

# Instructions:
# - Understand the problem clearly before responding.
# - Provide a structured and logical answer.
# - Use examples or code snippets if relevant.
# - Keep the explanation easy to follow and actionable.
# - Avoid unnecessary complexity unless required.

# Tone of the response:
# {tone_of_reply}

# Output Format:
# 1. Brief summary of the solution
# 2. Detailed explanation
# 3. Practical example (if applicable)
# 4. Final recommendation or conclusion

# Now generate the best possible response.

# """

# # print(os.getenv("api_key"))

# temp=PromptTemplate(
#     input_variables=["domain", "task", "tone_of_reply"],
#     validate_template=True,
#     template=template,
# )
# template=load_prompt('template.json')

# st.header("Expert Problem Solver :robot_face:") 
# domain=st.selectbox("Select Domain", ["Programming", "Data Science", "Machine Learning", "web development"])
# task=st.selectbox("Select Task", 
# [
#     "Explain this field", 
#     "key skills required to master this skill", 
#     "roadmap for this skill", 
#     "Scope of this field"
#     ])
# tone_of_reply=st.selectbox("Select Tone_of_reply", ["factual", "overview", "market trend analyzed reply", "recent research based reply"])

# # temp is not a function so u cant send values to it u have to add on through format
# if st.button("Generate Response"):
#     # result=model.invoke(temp(domain=domain, task=task, tone_of_reply=tone_of_reply))
#     final_prompt=template.format(domain=domain, task=task, tone_of_reply=tone_of_reply)
   
#     result=model.invoke(final_prompt)
#     st.write(result.content)


domain=st.selectbox("Select Domain", ["Programming", "Data Science", "Machine Learning", "web development"])
task=st.selectbox("Select Task", 
[
    "Explain this field", 
    "key skills required to master this skill", 
    "roadmap for this skill", 
    "Scope of this field"
    ])
tone_of_reply=st.selectbox("Select Tone_of_reply", ["factual", "overview", "market trend analyzed reply", "recent research based reply"])

template=PromptTemplate(
template="""
        You are an expert in {domain} with deep knowledge and practical experience.

        Your task is:
        "{task}"

        Instructions:
        - Understand the problem clearly before responding.
        - Provide a structured and logical answer.
        - Use examples or code snippets if relevant.
        - Keep the explanation easy to follow and actionable.
        - Avoid unnecessary complexity unless required.

        Tone of the response:
        {tone_of_reply}

        Output Format:
        1. Brief summary of the solution
        2. Detailed explanation
        3. Practical example (if applicable)
        4. Final recommendation or conclusion

        Now generate the best possible response.
    """,
input_variables=["domain", "task", "tone_of_reply"]
 

)

# prompt=template.invoke({
#     'task' : task,
#     'domain': domain,
#     'tone_of_reply': tone_of_reply


# })

# if st.button("Generate Response"):
#     result=model.invoke(prompt)
#     st.write(result.content)

# via chaining response 
if st.button("Generate Response"):
    chain=template | model
    result=chain.invoke({'task' : task,
    'domain': domain,
    'tone_of_reply': tone_of_reply
     })
    st.write(result.content)