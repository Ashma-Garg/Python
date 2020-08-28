xfile=open("findIntegerInString.py")
#open function go by sentence to sentence
count=0
for file in xfile:
    count=count+1
    if file.startswith("for"):
        print(file.rstrip())        #to eliminate extra line space
    #if not file.startwith("for")
print(count)
xfile=open("findIntegerInString.py")
yfile=xfile.read()
#read function go by char to char
count=0
for file in yfile:
    count=count+1
print(count)
