def balancedBrackets(string):
    # Write your code here.
	l=list()
	flag=False
	array=['(',')','[',']','{','}']
	if(string[0] in array and not array.index(string[0])%2==0):
	   return False
	for i in range(len(string)):
		if string[i] in array:
			index=array.index(string[i])
			if(index%2==0):
				l.append(string[i])
			else:
				last=l.pop()
				print(last)
				if(array.index(last)+1==index):
					flag=True
				else:
					return False
	if(len(l)):
		return False
    return flag
