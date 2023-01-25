"""74. Search a 2D Matrix


https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix `matrix` with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""


def search_matrix(matrix, target):
    """
    Binary search on rows
    Binary search in the row
    """

    row_search_result = binary_search_rows(matrix, target)

    if isinstance(row_search_result, bool):
        return row_search_result
    else:
        return binary_search_list(matrix[row_search_result], target)


def binary_search_rows(matrix, target):
    """Returns true if it finds the target, otherwise returns the row that may hold it"""

    if target < matrix[0][0] or target > matrix[-1][-1]:
        return False

    low_index = 0
    high_index = len(matrix)

    while True:
        midpoint_index = low_index + (high_index - low_index) // 2
        midpoint_value = matrix[midpoint_index][0]

        if midpoint_value == target:
            return True
        elif midpoint_value < target and high_index - midpoint_index <= 1:
            return midpoint_index
        elif midpoint_value > target:
            high_index = midpoint_index
        elif midpoint_value < target:
            low_index = midpoint_index


def binary_search_list(values, target):
    low_index = 0
    high_index = len(values)

    while True:
        midpoint_index = low_index + (high_index - low_index) // 2
        midpoint_value = values[midpoint_index]

        if midpoint_value == target:
            return True
        elif midpoint_value < target and high_index - midpoint_index <= 1:
            return False
        elif midpoint_value > target:
            high_index = midpoint_index
        elif midpoint_value < target:
            low_index = midpoint_index
