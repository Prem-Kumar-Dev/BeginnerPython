import numpy as np

def matrix_addition():
    print(np.add(matrix1,matrix2))

def matrix_subtraction():
    print(matrix1 - matrix2)

def matrix_multiplication():
    print(matrix1 * matrix2)

def matrix_division():
    print(matrix1 / matrix2)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

matrix_addition()
matrix_subtraction()
matrix_multiplication()
matrix_division()
