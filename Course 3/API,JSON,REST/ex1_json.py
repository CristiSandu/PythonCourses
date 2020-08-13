import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print(data)
info = json.loads(data)
print('User count:', len(info))
suma = 0
for into in info["comments"] :
    suma = suma + int( into["count"])

print(suma)