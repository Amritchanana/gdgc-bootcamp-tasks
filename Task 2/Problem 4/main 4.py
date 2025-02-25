# Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode

import numpy as np

def matrix_mean(matrix, mode):
    matrix = np.array(matrix)  # Converts to NumPy array for easy calculations
    
    if mode == 'row':
        return matrix.mean(axis=1).tolist()  # Mean for rows
    elif mode == 'column':
        return matrix.mean(axis=0).tolist()  # Mean for columns
    else:
        return -1

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix_mean(matrix, 'row'))    
print(matrix_mean(matrix, 'column'))