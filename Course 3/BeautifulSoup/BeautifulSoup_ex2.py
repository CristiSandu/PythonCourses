# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)

# Retrieve all of the anchor tags
index = 0
while index != count :

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    index = index + 1
    tags = soup('a')
    nr = 0
    for tag in tags:
        nr = nr + 1
        if nr == position :
            url = tag.get('href', None)
            print(tag.get('href', None))
            break
