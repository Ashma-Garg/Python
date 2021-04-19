# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=int(input())
mylist=list()

mylist=input().split(" ")
N=int(input())
lst=list()
for _ in range(N):
    lst.append(input().split())
d=dict()
d=Counter(mylist)
addition=0
for i in lst:
    if(d.get(i[0])):
        addition=addition+i[1]
        d[i[0]]=d.get(i[0])-1
    # print(i[0])
print(addition)
# print(Counter(**lst))
