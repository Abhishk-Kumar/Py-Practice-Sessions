# first para ,sentence , words, characters do this

from langchain_text_splitters import RecursiveCharacterTextSplitter
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
Once upon a time, in the golden kingdom of Aryavarta Kingdom, there lived a wise king named King Veerendra. He was loved by his people because he ruled with honesty, courage, and kindness.

The kingdom was rich with green forests, shining rivers, and busy marketplaces. But one year, a terrible drought struck the land. Crops failed, rivers dried up, and people began to suffer.

The royal ministers advised the king to increase taxes so the palace treasury would remain full. But King Veerendra refused.

Instead, he opened the royal food stores for the people and sold his own jewels to buy grain from nearby kingdoms. Every morning, he walked among the villagers, listening to their problems personally.

One day, an old farmer approached him and said,
“Your Majesty, why do you sacrifice your wealth for us?”

The king smiled and replied,
“A king’s true treasure is not gold. It is the happiness of his people.”

Inspired by the king’s kindness, the citizens united together. Some dug new wells, some shared food, and others helped farmers restore their lands. Slowly, the kingdom recovered from the drought.

Years later, travelers from distant lands came to hear the story of the king who chose his people over riches. King Veerendra became known as “The King with the Golden Heart.”

And from that day onward, the people of Aryavarta remembered one lesson forever:

A great ruler is not the one who sits on the richest throne, but the one who stands beside his people in difficult times.

"""
splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
  
)

# if pdf so split_documents will be used and if text so split_text will be used
result=splitter.split_text(text)
print(result)