'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

l=[1,2,3,4,5,1,2,3,4,1,2,3,5];
d=dict()
i=0
while(i<(len(l)-1)):
    flaf=False
    if((i+3)<len(l)):
        j=i+2
        while(j<(len(l)-1)):
            if(l[i]==l[j] and l[i+1]==l[j+1]):
                flag=True
                d[(l[i],l[i+1])]=d.get((l[i],l[i+1]),0)+1
                l.pop(j)
                l.pop(j)
            j=j+1
    if flag is True:
        i=i+1
    i=i+1

for key,value in d.items():
    print(key , "->" , value);
