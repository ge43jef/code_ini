import numpy as np

def flippedmatrix ( matrix ):
    max_element= float('-inf')
    index_i = -1
    index_j = -1
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element > max_element:
                max_element = element
                index_i = i
                index_j = j
    #bring highest elemnet to the top left corner
    matrix[[0,index_i]] = matrix[[index_i,0]]
    matrix[:,[0,index_j]] = matrix[:,[index_j,0]]
    return matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(flippedmatrix(matrix))