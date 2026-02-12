import sqlite3
#import requests 
import urllib.request
'''
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
'''
#url = input('url: ')
#if (len(url)<1): url= 'https://data.pr4e.org/mbox-short.txt'

#fh = urllib.request.urlopen(url,context=ctx)


#print(fh)


conn = sqlite3.connect('orgsdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER) ')

fname = input('Enter file name: ')
if(len(fname)<1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    #line = line.decode()
    if not line.startswith('From: '): continue
    pieces= line.split('@')
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?',(email,))
    row = cur.fetchone()
    if row is None: 
        cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)', (email,))
    else: 
        cur.execute('UPDATE Counts SET count = count +1 WHERE org = ?',(email,))
    
conn.commit()
sqlstr= 'SELECT * from Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(row)