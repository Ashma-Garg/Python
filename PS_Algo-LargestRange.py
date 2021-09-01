def largestRange(array):
    # Write your code here.
	array.sort()
	print(array)
	i=0
	start=0
	end=0
	i=0
	if(len(array)==1):
		return [array[0],array[0]]
	while(i<len(array)-1):
		j=i
		while(j<(len(array)-1) and array[j+1]-array[j]<=1):
			j+=1
		print(j)
		if((j-i)>(end-start)):
			start=array[i]
			end=array[j]
		i=j+1


    return [start,end]
