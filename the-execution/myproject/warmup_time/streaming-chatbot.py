from groq import Groq
import os

client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

stream=client.chat.completions.create(
   messages= [
        {
            "role":"system",
            "content":"You are a helpful assistant"
        },
       {
           "role":"user",
           "content":"Explain Fast api in python"
       }
    ],
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    stop=None,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
)

# for chunk in stream:
#     print(chunk.choices[0].delta.content, end="")

for chunk in stream:
    content=chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)