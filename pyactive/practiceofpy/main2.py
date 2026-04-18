# Aynchronous data fetcher 

import asyncio
import aiohttp
import argparse
from urllib.parse import quote
import json
import time


base_apiurl="https://en.wikipedia.org/api/rest_v1/page/summary"
results=[]


parser=argparse.ArgumentParser(description="CLI wikipedia data scraper")
parser.add_argument("topics", nargs="+", help="topics to be searched :")
arguments=parser.parse_args()
topics=arguments.topics
headers = {
    "User-Agent": "MyWikiCLI/1.0 (contact: abhishek@example.com)",
    "Accept": "application/json"
}


def get_tasks(session):
    tasks=[]
    titlelist=[]
    for title in topics:
        encoded_title=quote(title)
        titlelist.append(encoded_title)
        finalurl=f"{base_apiurl}/{encoded_title}"
        tasks.append(session.get(finalurl, headers=headers))
    print(titlelist)
    return tasks
    

async def get_data():
    starttime=time.time()
    async with aiohttp.ClientSession() as session:
        tasks=get_tasks(session)
        responses=await asyncio.gather(*tasks)
        for response in responses:
            async with response:
                if response.status == 200:
                    data=await response.json()
                    results.append(data)
                else:
                    print(f"error:", response.status)
        endtime=time.time()  
        
        print(json.dumps(results, indent=2))
        print(f"It took {endtime-starttime:2f} seconds to complete data scraping")
   
if __name__ == "__main__":
    asyncio.run(get_data())
        
