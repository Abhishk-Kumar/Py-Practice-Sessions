from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import os

api_key=os.getenv("api_key")
# print(api_key)
# for creative works use high temp ..for factual use low temp
# // token =words 
model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.8, max_completion_tokens=100, api_key=api_key )
res=model.invoke("what is capital of uttar pradesh")
print(res.content)