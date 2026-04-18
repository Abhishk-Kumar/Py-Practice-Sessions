
import os

directorypath=('/Users/abhishek/Desktop/Otakuhub')

contents=os.listdir(directorypath)

for item in contents:
    print(item)


a=int(input("enter no :"))
b=int(input("enter no2 :"))

res=a+b
print(res)
c=input("enter name")
print(f"good boi {c}")
a="abhi is here \n vut ghj"
print(a)