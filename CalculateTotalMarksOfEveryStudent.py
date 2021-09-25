stud="Stud1,20 Stud2,30 Stud1,10 Stud2,30"

l=[i.split(",") for i in stud.split(" ")]

d=dict()
for i in l:
    d[i[0]]=d.get(i[0],0)+int(i[1])
print(d)

# l is [['Stud1','20'],['Stud2','30'],['Stud1','10'],['Stud2','30']]
# Output={'Sud1':30,'Stud2':60}
