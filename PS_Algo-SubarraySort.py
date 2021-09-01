def subarraySort(array):
    # Write your code here.
	a=[-1,-1]

	for i in range(1,len(array)):
		if(array[i]<array[i-1]):
			for j in range(len(array)):
				if(array[j]>array[i]):
					temp=array.pop(i)
					array.insert(j,temp)
					if(a[0]<0 or j<a[0]):
						a[0]=j
					if(a[1]<0 or i>a[1]):
						a[1]=i
					break

	return a
