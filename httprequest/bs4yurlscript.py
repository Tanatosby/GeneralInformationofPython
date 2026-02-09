import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup as bs 

url = input('Enter: ')
html = urllib.request.urlopen(url).read().decode()
soup = bs(html,'html.parser')

tags = soup('a')
for tag in tags: 
    print(tag.get('href',None))