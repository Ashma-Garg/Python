# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
addition=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        pos=line.find(":")
        num=float(line[pos+1:])
        addition+=num
        count=count+1
print("Average spam confidence:",addition/count)
