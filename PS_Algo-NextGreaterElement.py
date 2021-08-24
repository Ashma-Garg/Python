def nextGreaterElement(array):
    # Write your code here.
	res=[-1]*len(array)
	for i in range(len(array)):
		# loop to go through a cicular loop...
		for j in range(i+1,len(array)+i):
			pos=j
			if(j>(len(array)-1)):
				pos=j-len(array)
			if(array[pos]>array[i]):
				res[i]=array[pos]
				break
    return res
