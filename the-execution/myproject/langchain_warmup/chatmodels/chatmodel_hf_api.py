from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
import os

api_key=os.getenv("hf_token")
# print(api_key)
# for creative works use high temp ..for factual use low temp
# // token =words 
# model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.8, max_completion_tokens=100, api_key=api_key )
# res=model.invoke("what is capital of uttar pradesh")
# print(res.content)
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama_v1.1",
    task="text-generation",
)
model=ChatHuggingFace(llm=llm)
res=model.invoke("what is capital of uttar pradesh")
print(res.content)

