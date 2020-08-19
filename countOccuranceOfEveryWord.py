name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
last=0
time=None
t=dict()
l=list()
for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        lst=line.split()
        time=lst[len(lst)-2]
        l=time.split(":")
        t[l[0]]=t.get(l[0],0)+1

lstnew=list()
for k,v in t.items():
    nl=(k,v)
    lstnew.append(nl)

lstnew=sorted(lstnew)
for k,v in lstnew:
    print(k,v)
