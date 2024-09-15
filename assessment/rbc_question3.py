sequence = [1, 2 , 0]


def find_sequence (matrix):
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