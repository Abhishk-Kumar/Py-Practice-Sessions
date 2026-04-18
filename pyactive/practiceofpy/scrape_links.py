import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



def main():
    currencylist_url='https://en.wikipedia.org/wiki/List_of_circulating_currencies'
    all_links=[]
    response=requests.get(currencylist_url)
    # parse in right format 
    soup=BeautifulSoup(response.text, 'lxml')
    current_element = soup.select('p+table td:nth-child(2) > a, p+table td:nth-child(1) > a:nth-child(1)')
    print(len(current_element))
    for link in current_element:
        url=link.get('href')
        final_url=urljoin(currencylist_url, url)
        all_links.append(final_url)

    with open('links.csv', 'w')as f:
        writer=csv.writer(f)
        for link in all_links:
            writer.writerow([link])

if __name__ == "__main__":
    main()



