# from langchain_groq import ChatGroq

# from dotenv import load_dotenv
# import os
# load_dotenv()

# llm=ChatGroq(model="llama-3.3-70b-versatile",  )

# result=llm.invoke("What is Capital of USA")
# print(result.content)


# api_key=os.getenv("api_key")
# # print(api_key)

# llm=ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key )

# result=llm.invoke("What is Capital of USA")
# print(result.content)

# old way llm => latest way is chat models ..llm give string input output both
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

llm=OpenAI(model='gpt-3.5-turbo-instruct')
result=llm.invoke("What is capital of india")
print(result)