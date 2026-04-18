# U4OZE60Q1E49F6D8.
# import requests
import time
import asyncio
import aiohttp
import json

url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey=U4OZE60Q1E49F6D8'
symbols=["GOOG", "IBM" , "TSLA", "MSFT" , "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM" , "TSLA", "MSFT", "IBM"]
results=[]
starttime=time.time()

def get_task(session):
    tasks=[]
    for symbol in symbols:
        tasks.append(asyncio.create_task(session.get(url.format(symbol), ssl=False)))
    return tasks
    

async def get_symbols():
    # session=aiohttp.ClientSession()
    # below way auto closes session 
    async with aiohttp.ClientSession() as session:   
       tasks=get_task(session)
       responses=await asyncio.gather(*tasks)
       for response in responses:
           results.append(await response.json()) 
           print("\n", results, "\n")
              

    # session.close() 
    # session.get gives session gives attributes like requests it give coroutine   
#  task way and gather way is used so can make list of tasks and send to event loop at once so all api call done at once instead waiting fr 1st response  

asyncio.run(get_symbols())
# loop=asyncio.get_event_loop()
# loop.run_until_complete(get_symbols())
# loop.close()


endtime=time.time()
totaltime=endtime-starttime
print(f"It took {totaltime} to make {len(symbols)} api calls")
 



