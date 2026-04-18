# from groq import Groq
# import os

# client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

# chat_completion=client.chat.completions.create(
#    messages= [
#         {
#             "role": "user",
#             "content": "Explain fast api in python"
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )

# print(chat_completion.choices[0].message.content)


# CLI tool to parse js of jobs and provide structured data 

from groq import Groq
import os
import json

client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

# user_input=input("Kindly paste your jd here : ")

prompt = """
Job Title: Junior AI Engineer — Remote (India)
Company: Nuvora Tech

We are looking for a Junior AI Engineer...
Salary: ₹6-10 LPA
Location: Remote (India based)
Experience: 0-1 years
"""

chat_completion=client.chat.completions.create(
messages=[{
    "role":"system",
    "content":"""You are job description parser. Return valid json data only nothing else.
    Fields: role, company, skills_required, salary, location, remote, experience_years,
    If any field not found, put null."""
},
{
    "role":"user",
    "content":f"Parse this job description and return json data only : {prompt}"

}
],
model="llama-3.3-70b-versatile",
)

response = chat_completion.choices[0].message.content
clean = response.replace("```json", "").replace("```", "").strip()
res = json.loads(clean)
print(res)
# res=json.loads(response)
# print(repr(response))
# print(json.dumps(response, indent=2))