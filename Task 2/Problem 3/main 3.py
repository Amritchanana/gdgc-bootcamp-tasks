# Write a Python function that reshapes a given matrix into a specified shape. if it cant be reshaped return back an empty list [ ]


def reshape_matrix(matrix, new_rows, new_cols):
    # Flattening the matrix into a 1D list
    flat_list = [num for row in matrix for num in row]
    
    # Checking if reshaping is possible
    if len(flat_list) != new_rows * new_cols:
        return []
    
    # Creating the new reshaped matrix
    reshaped_matrix = [flat_list[i * new_cols: (i + 1) * new_cols] for i in range(new_rows)]
    
    return reshaped_matrix

# Example Usage
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
new_shape = (4, 2)
result = reshape_matrix(matrix, *new_shape)
print(result)