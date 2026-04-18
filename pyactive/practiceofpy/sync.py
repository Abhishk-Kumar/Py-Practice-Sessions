# U4OZE60Q1E49F6D8.
import requests
import time


symbols=["GOOG", "IBM" , "TSLA", "MSFT" , "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT" , "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT"]
results=[]
# response=requests.get(url)
# data=response.json()
# print(data)
# def callapi():
starttime=time.time()
for symbol in symbols:
     url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey=U4OZE60Q1E49F6D8'
     print(f"Working on symbols: {symbol}")
     response=requests.get(url)
     results.append(response.json())
     print(results)
     print("\n")

endtime=time.time()
totaltime=endtime-starttime
print(f"It took {totaltime} to make {len(symbols)} api calls")
 



