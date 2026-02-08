import re

f = open(input('File: '))
try:

    str = f.read()
    y = re.findall('[0-9]+',str)
    sum(y)



except:
    print('error, this is not a file text')
    quit()