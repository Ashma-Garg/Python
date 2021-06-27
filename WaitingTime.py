def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
	add=0
	total=0
	i=0
	while(i<(len(queries)-1)):
		add=add+queries[i]
		total=total+add
		i=i+1
    return total
