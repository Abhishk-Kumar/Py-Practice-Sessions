from groq import Groq
import os

client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

messages=[
    {
        "role":"system",
        "content":"You are a helpful assistant",
    }
]

while True:
    prompt=input("Type your text here: ")
    if prompt == "exit":
        break
    else:
        messages.append({
            "role":"user",
            "content":prompt,
        })
    N=10 #last 10 messages
    window=[messages[0]] + messages[-N :]
    reply=client.chat.completions.create(
        messages=window,
        model="llama-3.3-70b-versatile",
    )
    response=reply.choices[0].message.content
  
    messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )
    print(response)

