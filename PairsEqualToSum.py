l=[2,3,7,9,5,0,2,7,4,6,0,1,7,8]
k=8
result=list()
d=dict()
for i in l:
    left=k-i
    if d.get(left):
        result.append([left,i])
    else:
        d[i]=1

print(result)

# result=[[3,5],[2,6],[7,1],[0,8]]
