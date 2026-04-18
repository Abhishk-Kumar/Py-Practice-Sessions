from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()


# embeddings=HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2',)

# text="What is capital of india"

# vector=embeddings.embed_query(text)
# print(str(vector))

embeddings=HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2',)

documents=["What is capital of india",
           "What is capital of uttar pradesh",
         ]

vector=embeddings.embed_documents(documents)
print(str(vector))