# first para ,sentence , words, characters do this

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_groq import ChatGroq

from dotenv import load_dotenv

import os

load_dotenv()

model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=800, 
    temperature=0.7
    )

text="""
# Python Class and Loop Example

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


# Creating objects
s1 = Student("Abhishek", 85)
s2 = Student("Rahul", 90)
s3 = Student("Ankit", 78)

# Storing objects in a list
students = [s1, s2, s3]

# Loop through objects
for student in students:
    student.display()

"""
splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
  
)

# if pdf so split_documents will be used and if text so split_text will be used
result=splitter.split_text(text)
print(result)