import pandas as pd

from bs4 import BeautifulSoup
import requests


url = 'https://finance.yahoo.com'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html')

class_header = 'title-text yf-1qzp9vr'
headers_soup = soup.find_all('span', class_=class_header)
headers_list = [header.text for header in headers_soup][1:5]

for index, header in enumerate(headers_list):
    class_id = 'dock yf-pmz4k'
    topMovers_soup = soup.find_all('ul', class_=class_id)[index] 
    topMovers_soup = topMovers_soup.find_all('span')

    topMovers_list = [topMovers_soup[i:i+4] for i in range(0, len(topMovers_soup), 5)]
    topMovers_list = [[topMover[i].text for i in range(4)] for topMover in topMovers_list]
    topMovers = pd.DataFrame(topMovers_list, columns=['Ticker', 'Company', 'Change', 'Change $'])
        


    print(f"{header}: ")
    print(topMovers)
    print()