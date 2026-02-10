import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
#url = 'https://en.wikipedia.org/wiki/IBM'
#url = 'https://finance.yahoo.com/quote/ETH-USD/history/'

url = input('Enter- ')
if len(url)<1:
    url = 'https://www.udep.edu.pe'
response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content,'html.parser')

#print(soup)
links = soup.find_all('a')
dicc = dict()
dicc['urls'] = []
for link in links:
    url = link.get('href')
    try:
        rel = re.findall('^https.+',url)
        if len(rel)<1:
            pass
        else:
            r = rel[0]
            #print(type(r))
            dicc['urls'].append(r)
    except:
        pass
df = pd.DataFrame(dicc)
df.to_excel('urls.xlsx')