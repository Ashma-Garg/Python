# Python3 Code For A Boolean Matrix Question
def modifyMatrix(mat):

	"""
	Initializes first row and column with a value of 1 if there is a 1 present in any
	position within them. It then propagates the presence of 1 to all other positions
	in the matrix based on the first row and column values.

	Args:
	    mat (List[List[int]] | List[Dict[int, int]]): 2D matrix representation of an
	        image, where each element at index `[i][j]` corresponds to a pixel in the
	        image.

	"""
	# variables to check if there are any 1
	# in first row and column
	row_flag = False
	col_flag = False

	# updating the first row and col
	# if 1 is encountered
	for i in range(0, len(mat)):

		for j in range(0, len(mat[0])):
			if (i == 0 and mat[i][j] == 1):
				row_flag = True

			if (j == 0 and mat[i][j] == 1):
				col_flag = True

			if (mat[i][j] == 1):
				mat[0][j] = 1
				mat[i][0] = 1

	# Modify the input matrix mat[] using the
	# first row and first column of Matrix mat
	for i in range(1, len(mat)):

		for j in range(1, len(mat[0])):
			if (mat[0][j] == 1 or mat[i][0] == 1):
				mat[i][j] = 1

	# modify first row if there was any 1
	if (row_flag == True):
		for i in range(0, len(mat[0])):
			mat[0][i] = 1

	# modify first col if there was any 1
	if (col_flag == True):
		for i in range(0, len(mat)):
			mat[i][0] = 1

# A utility function to print a 2D matrix


def printMatrix(mat):

	"""
	Iterates through each element in a given matrix and prints it to the console. It
	does so by iterating over each row, then printing all elements in that row before
	moving on to the next.

	Args:
	    mat (List[List[int]] | List[List[float]] | List[List[str]]): 2-dimensional,
	        containing elements that can be integers, floats or strings. It represents
	        a matrix to be printed.

	"""
	for i in range(0, len(mat)):
		for j in range(0, len(mat[0])):
			print(mat[i][j], end="")

		print()


# Driver Code
mat = [[0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0]]

print("Input Matrix :")
printMatrix(mat)

modifyMatrix(mat)

print("Matrix After Modification :")
printMatrix(mat)

# This code is contributed by Nikita tiwari.
