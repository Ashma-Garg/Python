sequence = [1, 2 , 0]


def find_sequence (matrix):
    """
    Identifies the maximum length pattern of '1's in a given binary matrix using
    a sequential search approach. It iterates over each cell with value '1' and
    extends its sequence horizontally, vertically, or diagonally, updating the
    maximum length if necessary.

    Args:
        matrix (List[List[int]]): 2D array-like data structure consisting of zeros
            and ones. It represents a matrix or grid containing pixel values, where
            1 indicates a relevant cell for the sequence length calculation.

    """
    seq = [2, 0]

    ROW = len(matrix)
    COL = len(matrix[0])
    seq_pos = 0
    final_count = 0
    for i in range(ROW):
        for j in range(COL):
            if matrix[i][j] == 1:
                dr = [-1, 1, 1, -1]
                dc = [1, 1, -1, -1]
                for k in range(len(dr)):
                    max_pattern_len = 1
                    a = cal_seq_len(matrix, i, j, seq, seq_pos, max_pattern_len, dr[k], dc[k])
                    final_count = max(final_count, a)

    print(final_count)


def cal_seq_len (matrix, row_p, col_p, seq, seq_pos, max_pattern_len, dr_pos, dc_pos):
    """
    Performs a depth-first search on a matrix to find the longest pattern matching
    a given sequence. It explores adjacent cells, checks if their values match the
    next character in the sequence, and updates the maximum pattern length accordingly.

    Args:
        matrix (List[List[int]]): 2D array representing a grid or table with integer
            values. Its dimensions are n x m, where each element at position (i,
            j) is denoted by matrix[i][j].
        row_p (int): The row index of the current position being evaluated in the
            matrix. It represents the current vertical (row) coordinate.
        col_p (int): Used to represent the column position of the current cell
            being examined in the matrix during recursive sequence length calculation.
            It serves as an input for movement direction calculations.
        seq (str | Sequence[int, str, Sequence...]): Used to store a sequence of
            characters or values for pattern matching with a given matrix at the
            specified position.
        seq_pos (int): 0 or 1, used to access elements at even or odd positions
            respectively from the sequence `seq`. It is updated within the function
            as it progresses through the sequence.
        max_pattern_len (int | None): Used to keep track of the maximum length of
            a sequence found so far in the matrix that matches the given pattern
            `seq`. It starts at zero.
        dr_pos (int): 1-based, used to access the elements of lists `dr`. It defines
            the direction (row) position for the next cell in the sequence. Its
            values are: 0 (top), 1 (bottom-left), 2 (bottom-right), or 3 (left).
        dc_pos (int): 1-indexed. It indicates the position of the next cell to be
            visited horizontally relative to the current position, with values
            ranging from 0 (right) to 3 (left).

    Returns:
        int: The maximum length of a pattern that matches a given sequence within
        a matrix from a specified starting position.

    """
    dr = [-1, 1, 1, -1]
    dc = [1, 1, -1, -1]

    seq_pos = (seq_pos % 2)
    
    newR = row_p + dr[dr_pos]
    newC = col_p + dc[dc_pos]

    if(0 <= newR < len(matrix) and 0 <= newC < len(matrix[0])):
            if matrix[newR][newC] == seq[seq_pos]:
                max_pattern_len += 1

                max_pattern_len = cal_seq_len(matrix, newR, newC, seq, seq_pos + 1, max_pattern_len, dr_pos, dc_pos)
            else:
                 return max_pattern_len
            
    return max_pattern_len



matrix =[
    [1, 1, 0, 2, 0],
    [2, 2, 2, 0, 1], 
    [0, 2, 1, 1, 2], 
    [2, 1, 1, 2, 0]
]
find_sequence(matrix)