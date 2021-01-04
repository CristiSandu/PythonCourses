 
# line ="https://www.tabulaturi.ro/artisti/augustin-fratila";
# pieces = line.split('/')
# name = pieces[4]
# name = name.upper()
# print(name)
import sqlite3

conn = sqlite3.connect('artistsdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Html_dark;
''')
