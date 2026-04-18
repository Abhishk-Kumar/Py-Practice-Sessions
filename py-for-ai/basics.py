import requests

response=requests.get("https://api.github.com")

print(response.status_code)

age=24

# fstrings 
# import math

# from math import sqrt,pi

# num=sqrt(16)

# print(num)

# import datetime

# date=datetime.date.today()
# print(date)

import os
current_directory=os.getcwd()
print(current_directory)

name="abhi"
string=f"hii my name is {name.upper()} !"
print(string.title())
prin=string.replace("ABHI", "Amit")
print(prin)


print(78+90)