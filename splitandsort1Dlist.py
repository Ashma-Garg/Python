fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    l=line.split()
    for i in range(len(l)):
        if l[i] in lst:
            continue
        else:
            lst.append(l[i])
lst.sort()
print(lst)
