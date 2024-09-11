# A pronic number is a number which is the product of two consecutive integers.
import math
"""def is_pronic(n):
    number = int(math.sqrt(n))
    return n == number * (number + 1)

print(is_pronic(11))"""

# 2ex: Rotate a Matrix by 90 Degrees Clockwise

'''def rotate_matrix(matrix):
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
print(matrix)'''

#Problem: Longest Consecutive Subsequence
#Description:
#Given an unsorted array of integers, find the length of the longest consecutive subsequence. 
#A consecutive subsequence is a sequence of numbers where each number follows the previous one
#                         with a difference of exactly one.

def longestConsecSubseq(nums):
    num_set = set(nums)  # Convert input list to a set
    longest_streak = 0
    # Loop through each number
    for num in nums:
        # Check if it is the start of a sequence 
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            #how long the sequence continues
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak

nums = [1, 4, 9, 5, 90, -4, -10, 3, 6, 7]
print('the longest cons subseq is ', longestConsecSubseq(nums))

