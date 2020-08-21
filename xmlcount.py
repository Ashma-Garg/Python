import urllib.request
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
add=0
url=input('Enter-')
html=urllib.request.urlopen(url,context=ctx).read()
h=html.decode("utf-8")      #html was in byte. to change it in string we used decode() and stored it in other variable
stuff=ET.fromstring(h)
counts=stuff.findall('comments/comment/count')      #could also write it as './/count'
for c in counts:
    add+=int(c.text)
print(add)
