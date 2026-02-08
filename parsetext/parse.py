import re

try:
    f = open(input('File: '))
    str = f.read()
    y = re.findall('[0-9]+',str)
    y = [int(i) for i in y ]
    print('there are',len(y),'elements and the sum is:',sum(y))
    


except:
    print('error, this is not a file text')
    quit()
