def minimumCharactersForWords(words):
	fd=dict()
    # Write your code here.
	for i in words:
		d=dict()
		for j in i:
			d[j]=d.get(j,0)+1
			fd[j]=max(d.get(j,0),fd.get(j,0))
	arr=list()
	for key,value in fd.items():
		for j in range(int(value)):
			arr.append(key)
    return arr
