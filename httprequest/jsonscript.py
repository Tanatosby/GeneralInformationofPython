'''

Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2370290.json (Sum ends with 85)

'''

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
