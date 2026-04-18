from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os

load_dotenv()

embeding=HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2',)

documents = [
    "Virat Kohli is one of the best batters in modern cricket",
    "Jasprit Bumrah is known for his deadly yorkers and wicket-taking ability",
    "AB de Villiers was famous for his 360-degree batting style",
    "Rohit Sharma is called the Hitman for his explosive batting",
    "MS Dhoni is one of the greatest finishers and captains in cricket history",
    "Sachin Tendulkar is known as the God of Cricket for his legendary career",
    "Ben Stokes is a powerful all-rounder who performs well under pressure"
]

query="Tell me something about Rohit  "

doc_embedingVector=embeding.embed_documents(documents)
query_embedingVector=embeding.embed_query(query)

scores=cosine_similarity([query_embedingVector], doc_embedingVector)[0]
index, score=sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print("highest match index is :", index)
print("highest similarity score is :", score)