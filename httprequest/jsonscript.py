import json

import urllib.request
#from bs4 import BeautifulSoup as bs
url = input('Enter- ')

if len(url)<1:
    #url = "http://py4e-data.dr-chuck.net/comments_42.json" 
    url = 'http://py4e-data.dr-chuck.net/comments_2370290.json'

html = urllib.request.urlopen(url)

data = html.read().decode()

'''
data = 
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]
'''
n = list()
info = json.loads(data)
for item in info['comments']:
    n.append(item['count'])
print(sum(n))
'''
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
'''