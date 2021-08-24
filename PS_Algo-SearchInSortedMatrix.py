# this solution is total wastage. Actual solution is of only 15 lines and very simple code, not so complex
def searchInSortedMatrix(matrix, target):
    # Write your code here.
	pos=list()
	for i in range(len(matrix)):
		if(target<matrix[i][int(len(matrix[i])/2)]):
			pos=sortedMatrixTarget(matrix[i][:int(len(matrix[i])/2)],target,0,i)
			if(pos):
				return pos
		elif(target>matrix[i][int(len(matrix[i])/2)]):
			pos=sortedMatrixTarget(matrix[i][(int(len(matrix[i])/2)+1):],target,int(len(matrix[i])/2)+1,i)
			if(pos):
				return pos
		else:
			return [i,int(len(matrix[i])/2)]
	if not pos:
		pos=[-1,-1]
	return pos

def sortedMatrixTarget(matrix,target,j,s):
	i=0
	if(len(matrix)==0):
		return
	if(target<matrix[int(len(matrix)/2)]):
			pos=sortedMatrixTarget(matrix[:int(len(matrix)/2)],target,j,s)
	elif(target>matrix[int(len(matrix)/2)]):
			pos=sortedMatrixTarget(matrix[(int(len(matrix)/2)+1):],target,j+int(len(matrix)/2)+1,s)
	else:
			print(s,j,"hhg")
			return [s,j+int(len(matrix)/2)]

	return pos
