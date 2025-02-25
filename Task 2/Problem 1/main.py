# Write a Python function that takes the dot product of a matrix and a vector.return -1 if the matrix could not be dotted with the vector

import numpy as np

def dot_product(matrix,vector):
    matrix=np.array(matrix)
    vector=np.array(vector)

    if matrix.shape[1] != vector.shape[0]:
        return -1
    
    return np.dot(matrix, vector)

matrix = [[1, 2], [3, 4]]
vector = [1, 8]
result=dot_product(matrix,vector)
print(result)