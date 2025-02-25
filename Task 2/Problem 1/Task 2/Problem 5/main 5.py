# Write a Python function that multiplies a matrix by a scalar and returns the result

import numpy as np

def scalar_multiplication(matrix, scalar):
    matrix = np.array(matrix)  # Converts to NumPy array for easy computation
    result = matrix * scalar   # Performs scalar multiplication
    return result.tolist()     # Convert back to a list of lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

scalar = 2

result = scalar_multiplication(matrix, scalar)
print(result)