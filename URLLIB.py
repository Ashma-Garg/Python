import urllib.request
from bs4 import BeautifulSoup

import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter-')
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
add=0
tags=soup('span')
for tag in tags:
    a=int(tag.contents[0])
    #a=tag.get('span',None)
    add=add+a
    #print(tag.contents[0])
print(add)
