from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.tabulaturi.ro/litere/"
lst_link_litere = list()

for i in range(32) :
    lst_link_litere.append(url + str(i) )

list_link = list()
for j in lst_link_litere :
    #print(j)
    url = j
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')

    for tag in tags :
        if len(tag.get('href',None)) > 1 :
            if tag.get('href',None) in list_link:
                continue 
            else:
                list_link.append(tag.get('href',None))
                

        
conn = sqlite3.connect('artistsdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Artists')

cur.execute('''
CREATE TABLE Artists (Name TEXT, Link TEXT)''')

for line in list_link:
    if not line.startswith('https://www.tabulaturi.ro/artisti/'): continue
    pieces = line.split('/')
    name = pieces[4]
    name = name.upper()
    #cur.execute('SELECT  FROM Artists WHERE Name = ? ', (name,))
    row = cur.fetchone()
    cur.execute('''INSERT INTO Artists (Name, Link)
                VALUES (?, ?)''', (name,line))
    
    conn.commit()    


    

