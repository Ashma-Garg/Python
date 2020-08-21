import xml.etree.ElementTree as ET
add=0
input='''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>002</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''
print(type(input))
stuff=ET.fromstring(input)
print(stuff)
counts=stuff.findall('users/user')
for c in counts:
    print("Name",c.find('name').text)
    print("Attribute",c.get("x"))
