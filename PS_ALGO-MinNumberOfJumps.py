def minNumberOfJumps(array):
    
	count=0
	i=0
	while(i<len(array)-1):
		count=count+1
		if((i+array[i])<(len(array)-1)):
			arr=array[(i+1):(i+array[i]+1)]
			maxValue=0
			nextJumpLocation=i
			for j in range(len(arr)):
				if(arr[j]>=maxValue):
					if((i+array[i])>=(i+j+1+arr[j])):
						array[i+j+1]=0
					else:
						nextJumpLocation=i+j
						maxValue=arr[j]
			i=nextJumpLocation+1
		else:
			break
    return count
