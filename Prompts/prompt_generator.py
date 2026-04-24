from langchain_core.prompts import PromptTemplate


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

"""


# print(os.getenv("api_key"))

temp=PromptTemplate(
    input_variables=["domain", "task", "tone_of_reply"],
    validate_template=True,
    template=template,
)

temp.save('template.json')