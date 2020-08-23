from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.tabulaturi.ro/acorduri/fara-zahar/d-la-munte-10648"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup()
finalist = list()
nr = 0
print(type(html))

html2 = html.decode()
print(type(html2))
html2 = html2.replace("<body>",'''<body style="background-color:black">''')
html2 = html2.replace('''<pre class="tab-text">''','''<pre class="tab-text"  style="color:white"  >''')
html2 = html2.replace('''<div id="cardTab" class="card">''','''<div id="cardTab" class="card" style="background-color:black">''')
#print(html3)
#html3 = re.sub('<body style="background-color:black">.+            <div id="cardTab" class="card" style="background-color:black">','',html2)
#print(html3)

tags = soup('h1')
list_tracks = list()
for tag in tags :
   # if len(tag.get(None,None)) == 1 :
    list_tracks.append(tag.string)
    print(tag.string)
    name6 = tag.string
    name6_pice = name6.split(' - ')
    print(name6_pice[1])

#print(html2)
text_file = open("sample.html", "w")
n = text_file.write(html2)
text_file.close()


    


    #    print("dupa     ",tag)

    #print('Attrs:', tag.attrs)