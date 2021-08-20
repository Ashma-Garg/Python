boolean=1
def removeIslands(matrix):
    # Write your code here.
	visited=list()
	row=len(matrix)
	col=len(matrix[0])
	for i in range(len(matrix)):
		visited.append([0])
		for j in range(1,len(matrix[0])):
			visited[i].append(0)
	l=list()
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			boolean=1
			if(matrix[i][j]==1 and visited[i][j]==0):
				boolean=removeIslandsArray(matrix,visited,row,col,i,j,l,boolean)
	return matrix
def removeIslandsArray(matrix,visited,row,col,i,j,l,boolean):
	if(i<row and j<col and i>=0 and j>=0):
		if(matrix[i][j]==1 and visited[i][j]==0):
			if(i>0 and j>0 and i<row-1 and j<col-1 and boolean==1):
				l.append([i,j])
			else:
				l.clear()
				boolean=0
				if(i==row-1 or j==col-1):
					return boolean
			visited[i][j]=1
		else:
			return boolean
	else:
		return boolean
	boolean=removeIslandsArray(matrix,visited,row,col,i,j+1,l,boolean)
	boolean=removeIslandsArray(matrix,visited,row,col,i+1,j,l,boolean)
	boolean=removeIslandsArray(matrix,visited,row,col,i,j-1,l,boolean)
	boolean=removeIslandsArray(matrix,visited,row,col,i-1,j,l,boolean)

	for i in range(len(l)):
		matrix[l[i][0]][l[i][1]]=0
	return boolean
