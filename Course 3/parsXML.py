import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#commentinfo/comments/comment

while True:
    url = input('Enter url: ')
  
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
   
    tree = ET.fromstring(data)

    counts = tree.findall('.//comment')
    print(counts)
    suma = 0
    for index in counts :
        print(index.find('count'))
        suma = suma + int(index.find('count').text)

    print(suma)
