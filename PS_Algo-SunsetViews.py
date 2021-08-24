def sunsetViews(buildings, direction):
    # Write your code here.
	res=list()

	for i in range(len(buildings)):
		if(direction=='EAST'):
			b=buildings[i+1:]
		else:
			b=buildings[:i]
		if(not b):
			res.append(i)
		elif(not max(b)>=buildings[i]):
			res.append(i)


    return res
