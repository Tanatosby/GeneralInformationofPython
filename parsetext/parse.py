import re

try:
    f = open(input('File: '))
    str = f.read()
    y = re.findall('[0-9]+',str)
    y = [int(i) for i in y ]
    print('there are',len(y),'elements and the sum is:',sum(y))
    #print('there are',len([int(i) for i in re.findall('[0-9]+',f.read())]),'elements and the sum is:',sum([int(i) for i in re.findall('[0-9]+',f.read())]))


except:
    print('error, this is not a file text')
    quit()

