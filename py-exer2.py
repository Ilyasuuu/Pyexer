# A pronic number is a number which is the product of two consecutive integers.
import math
"""def is_pronic(n):
    number = int(math.sqrt(n))
    return n == number * (number + 1)

print(is_pronic(11))"""

# 2ex: Rotate a Matrix by 90 Degrees Clockwise

def rotate_matrix(matrix):
    matrix_len = len(matrix)
    for row in range(matrix_len):
        for col in range(row, matrix_len):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    for row in range(matrix_len):
        matrix[row].reverse()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]            
rotate_matrix(matrix)
print(matrix)