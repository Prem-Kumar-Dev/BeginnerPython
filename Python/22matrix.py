import numpy as np

def matrix():
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            a=int(input("Enter element of matrix:_"))
            row.append(a)
        matrix.append(row)
    print(matrix)
    return matrix

def matrix_addition():
    print("Addition:",np.add(matrix1,matrix2))

def matrix_subtraction():
    print("Subtraction:",np.subtract(matrix1,matrix2))

def matrix_multiplication():
    print("Multiply:",np.multiply(matrix1,matrix2))

rows = 2
columns = 2

matrix1=matrix()
matrix2=matrix()

matrix_addition()
matrix_subtraction()
matrix_multiplication()