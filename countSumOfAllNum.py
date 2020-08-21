import re
handle=open("data.txt")

lst=list()
newlst=list()
for line in handle:
    lst=re.findall("[0-9]+",line)
    for l in lst:
        newlst.append(int(l))
add=sum(newlst)
print(add)
