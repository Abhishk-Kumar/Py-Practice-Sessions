# ClI tool to get info from wikipedia 

# import requests
# from urllib.parse import quote


# base_apiurl="https://en.wikipedia.org/api/rest_v1/page/summary"
# title=input("Enter your title to search: ").strip()


# encoded_title=quote(title)
# final_url=f"{base_apiurl}/{encoded_title}"
# print(final_url)

# headers={
#     "User-Agent": "MyWikipediaCLI/1.0 (learning project)"
# }


# response=requests.get(final_url, headers=headers)
# print(response.url)



# if response.status_code == 200:
#     data=response.text
#     data2=response.json()
#     print(f"Response received sucessfully :200 {data}")
#     print(f"Response received sucessfully :200 {data2}")
# else:
#     print("there has been some error while calling")
#     print(f"ERROR: {response.status_code}")


# sequential fetcher 

# import requests
# from urllib.parse import quote
# import argparse

# parser=argparse.ArgumentParser(description="CLI tool")

# parser.add_argument("topics", nargs="+", help="topic to be searched")

# args=parser.parse_args()

# topics=args.topics
# print(topics)

# base_apiurl="https://en.wikipedia.org/api/rest_v1/page/summary"

# headers={
#     "User-Agent":"MywikiCLITool/1.0"
# }

# for title in topics:
#     encoded_title=quote(title)
#     final_url=f"{base_apiurl}/{encoded_title}"
#     response=requests.get(final_url, headers=headers)
#     if response.status_code == 200:
#         print(f"Response received sucessfully for {encoded_title}:{response.status_code}\n")
#         print("\n", response.json(), "\n")
#     else:
#         print(f"There has been some error: {response.status_code}")
      


# asynchronous fetcher 
import requests
import asyncio
import aiohttp
from urllib.parse import quote
import argparse

parser=argparse.ArgumentParser(description="CLI tool")

parser.add_argument("topics", nargs="+", help="topic to be searched")

args=parser.parse_args()

topics=args.topics
print(topics)

base_apiurl="https://en.wikipedia.org/api/rest_v1/page/summary"
headers={
    "User-Agent":"MywikiCLITool/1.0"
}

async def call_api(url):
        async with aiohttp.ClientSession() as session:
            async with session.get (url) as response:
                data=await response.json()
                return data
                               
async def main():
        
        result=await call_api(final_url, headers=headers)
        if result.status_code == 200:
            print(f"Response received sucessfully for {encoded_title}:{result.status_code}\n")
            print("\n", result.json(), "\n")
        else:
             print(f"There has been some error: {result.status_code}")
             print(result, "\n")


for title in topics:
    encoded_title=quote(title)
    final_url=f"{base_apiurl}/{encoded_title}"

   
    
    

if __name__=="main":
    asyncio.run(main())

































# import pandas  as pd


# def main():
#     print("Hello from pyactive!")
#     pd.to_read("../data/saless.csv")

# oop practice
# class Employee:
#     pass
# class Employee:
#     def __init__(self, name, email):
#         self.name=name
#         self.email=email

# emp1=Employee(name="abhi1",email="abhi1test@gmail.com")
# emp2=Employee(name="abhi2", email="abhi2gmail.com")

# print(emp1, emp2)

# emp1.name="Abhishek"
# emp1.email="abhishkdk@gmail.com"

# emp2.name="amit"
# emp2.email="amit@gmail.com"

# print(emp1.email)
# print(emp2.name)


# import asyncio

# async def main():
#     print("..hello")
#     print("from")
#     await asyncio.sleep(3)
#     print("world")

# asyncio.run(main())