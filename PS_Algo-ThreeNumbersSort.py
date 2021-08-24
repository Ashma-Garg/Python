def threeNumberSort(array, order):
    # Write your code here.
	# res=[0]*len(array)
	count=[0]*len(order)
	for i in range(len(order)):
		count[i]=array.count(order[i])
	k=0
	for i in range(len(order)):
		for j in range(count[i]):
			array[k]=order[i]
			k+=1
	return array

#Solution 2:

def threeNumberSort(array, order):
    # Write your code here.
	res=[0]*len(array)
	k=0
	for i in order:
		for j in range(array.count(i)):
			res[k]=i
			k+=1

    return res
