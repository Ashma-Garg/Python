name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
counts=dict()
for line in handle:
    if line.startswith("From:"):
        lst=line.split()
        counts[lst[1]]=counts.get(lst[1],0)+1

count=None
word=None
for key,value in counts.items():
    if count is None or count<value:
        count=value
        word=key

print(word,count)

#we could also use
# for key in counts:
#   if count is None or count<counts[key]
#       count=counts[key]
#       word=key
