def minimumPassesOfMatrix(matrix):
    # Write your code here.
	boolean=1
	row=len(matrix)
	col=len(matrix[0])
	count=-1
	# previous total negative numbers
	prevneg=-1
	# current total negatice numbers
	currneg=0

	# while there are any negative value run this loop
	while(boolean==1):
		# an array to store changed values after making them positive
		arr=[[0 for j in range(col)]for i in range(row)]
		count=count+1

		# change boolean value so that loop may be occur infinite loops
		boolean=0

		# fetch current negative vlaues
		currneg=containsNegative(matrix)

		# determine if there are no more possible changes
		if(prevneg==currneg):
			return -1
		elif(currneg==0):
			return 0
		else:
			prevneg=currneg
			for i in range(len(matrix)):
				for j in range(len(matrix[0])):
					# excute code only if value is negaitve
					if(matrix[i][j]<0):
						res=deterMatrix(arr,matrix,row,col,i,j)
						if(res==0):
							boolean=1
					else:
						arr[i][j]=matrix[i][j]

		matrix=arr
	return count+1
def containsNegative(matrix):
	cn=0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if(matrix[i][j]<0):
				cn+=1
	return cn
def deterMatrix(arr,matrix,row,col,i,j):
	# toggle variable if there is any positive number around negative number
	b=0
	b=deter(matrix,row,col,i+1,j,b)
	b=deter(matrix,row,col,i-1,j,b)
	b=deter(matrix,row,col,i,j+1,b)
	b=deter(matrix,row,col,i,j-1,b)
	if(b==1):
		arr[i][j]=matrix[i][j]*(-1)
	else:
		arr[i][j]=matrix[i][j]
	return b

def deter(matrix,row,col,i,j,b):
	if(i>=0 and j>=0 and i<=row-1 and j<=col-1):
		if(matrix[i][j]>0):
			return 1
		else:
			return b
	else:
		return b
