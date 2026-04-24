# from langchain_core.prompts import ChatPromptTemplate

# chat_template=ChatPromptTemplate([
#     ('system', "You are an helpful {domain} assistant"),
#     ('human', "what is {task} explain")
# ])

# prompt=chat_template.invoke({'domain':"cricket", 'task':"capital of india"})
# print(prompt)

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template=ChatPromptTemplate([
    ('system', "You are helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}')
])

# load chat history 
chat_history=[]
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)
prompt=chat_template.invoke({'query':"What is order status", 'chat_history': chat_history})
print(prompt)