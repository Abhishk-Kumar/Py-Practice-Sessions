from groq import Groq
import os

client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

jd_text = """
Job Title: Junior AI Engineer — Remote (India)
Company: Nuvora Tech

We are looking for a Junior AI Engineer...
Salary: ₹6-10 LPA
Location: Remote (India based)
Experience: 0-1 years
"""

# jd parser function 

def parse_jd(jd_text):
    response=client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":"""You are job description parser.Return valid json data only with no backticks and all.
                field:company, role, salary, remote, skills_required, location, experience_years.
                if any field is not present put None.
                """
            },
           { "role":"user",
              "content": f"Parse this job description and return json data only : {jd_text}"
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    jd_data=response.choices[0].message.content
    return jd_data

def chat_about_jd(jd_data):
    history=[]
    while True:
        userinput=input("Type your question regarding job description: ")
        if userinput == "exit":
            break
        else:
            history.append({"role":"user", "content":userinput })
            system_mesg=[{"role":"system", "content":f"You are a jd analyzer assistant {jd_data}"}]
           
        N=10
        window=[system_mesg[0]]+ history[-N:]
        stream=client.chat.completions.create(
            messages=window,
            model="llama-3.3-70b-versatile",
            stream=True,
            stop=None,
            temperature=0.5,
            top_p=1,
            max_completion_tokens=1024
        )
        full_reply=""
        for chunk in stream:
            content=chunk.choices[0].delta.content
           
            if content:
                print(content, end="", flush=True)
                full_reply += content
                
        print()
        history.append({ "role":"assistant", "content":content } )

def main():
    jd_data=parse_jd(jd_text)
    print(jd_data)
    chat_about_jd(jd_data)
   
   

if __name__=="__main__":
    main()

                