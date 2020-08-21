import urllib.request,urllib.parse,urllib.error
import json

url="http://py4e-data.dr-chuck.net/comments_906852.json"
add=0
html=urllib.request.urlopen(url).read()
stuff=html.decode()

s=json.loads(stuff)

for c in s['comments']:
    add=add+int(c['count'])
print(add)
