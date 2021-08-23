def validStartingCity(distances, fuel, mpg):
    # Write your code here.
	total=list()
	for i in range(len(fuel)):
		total.append(mpg*fuel[i])
	index=0
	l=len(total)
	for i in range(len(total)):
		if(total[i]<distances[i]):
			index=i+1
		elif(total[i]>distances[i]):
			if i<l-1:
				total[i+1]=total[i+1]+total[i]-distances[i]
			else:
				total[0]=total[0]+total[i]-distances[i]

    return index
