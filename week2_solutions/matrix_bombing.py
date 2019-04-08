def matrix_bombing_plan(m):
    bombing_plan = {}
    for index_row, row in enumerate(m):
        for index_col, col in enumerate(m[index_row]):
            new_matrix = [x[:] for x in m]
            new_matrix[]











def change_values(row, col, matrix)():
    reducer_value = matrix[row][col]
    value_to_change = matrix[row + 1][col]
    if row + 1 >= len(matrix)
        if matrix[row + 1][col] >= reducer_value:
            matrix[row + 1][col] = value_to_change - reducer_value
        else:
           matrix[row + 1][col] = 0
    if 






# matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
1 2 3
1 2 3
1 2 3