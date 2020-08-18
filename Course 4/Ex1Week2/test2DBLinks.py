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

#cur.execute('DROP TABLE IF EXISTS Artists')

cur.executescript('''
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Artists;


CREATE TABLE Artists (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE,
    link_artist TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    artist_id  INTEGER,
    link_track TEXT UNIQUE
);''')



for line in list_link:
    if not line.startswith('https://www.tabulaturi.ro/artisti/'): continue
    pieces = line.split('/')
    name = pieces[4]
    if line == "https://www.tabulaturi.ro/artisti/":
            continue
    print(name)
    name2 = name
    name = name.upper()
   
    #cur.execute('SELECT  FROM Artists WHERE Name = ? ', (name,))
    row = cur.fetchone()
    cur.execute('''INSERT OR IGNORE INTO Artists (name, link_artist)
                VALUES (?, ?)''', (name,line))
    cur.execute('SELECT id FROM Artists WHERE name = ? ', (name, ))
    artist_id = cur.fetchone()[0]

    list_tracks = list()

    url = line
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')

    for tag in tags :
        if len(tag.get('href',None)) > 1 :
            if tag.get('href',None) in list_link:
                continue 
            else:
               list_tracks.append(tag.get('href',None))

    for track in list_tracks :
        link_name_track = 'https://www.tabulaturi.ro/acorduri/'+ name2
        if not track.startswith(link_name_track): continue
        pieces = track.split('/')
        name = pieces[5]
        print("     " + name)
        name = name.upper()
        cur.execute('''INSERT OR REPLACE INTO Track
        (title, artist_id, link_track) 
        VALUES ( ?, ?, ?)''', 
        ( name, artist_id, track) )



    
    conn.commit()    


    
#"SELECT Track.title, Artists.name, Artists.id 
#    FROM Track JOIN Artists 
#    ON Track.artist_id = Artists.id   
#    ORDER BY Track.title"
