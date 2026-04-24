from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import os
import json
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


model=ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("api_key"), temperature=0.5, max_tokens=500)
context_history=[
    SystemMessage(content="You are a helpful ai assistant"),
    # HumanMessage(content="What is capital of France?"),
]
while True:
    user_input= input("User : ")
    context_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        # print(context_history)
        break
    response=model.invoke(context_history)
    context_history.append(AIMessage(content=response.content))
    print("AI: ", response.content)

print(context_history)
# if user_input == "exit":
#     print( json.dumps(context_history, indent=4))
 # adds newline

   

