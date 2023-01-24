"""36. Valid Sudoku

https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""


def is_valid_sudoku(board):
    # validate rows
    rows_valid = all([has_no_duplicates(skip_empty(row)) for row in board])

    # validate columns
    columns = []
    for i in range(9):
        columns.append([row[i] for row in board])

    columns_valid = all(has_no_duplicates(skip_empty(col)) for col in columns)

    # validate sub-boxes
    sub_boxes = [[[] for _ in range(3)] for _ in range(3)]

    for i, row in enumerate(board):
        for j, value in enumerate(row):
            sub_boxes[i // 3][j // 3].append(value)

    for row in sub_boxes:
        for box in row:
            has_no_duplicates(box)

    sub_boxes_valid = all([all([has_no_duplicates(skip_empty(box)) for box in row]) for row in sub_boxes])

    return rows_valid and columns_valid and sub_boxes_valid


def skip_empty(enumerable, empty_char='.'):
    for item in enumerable:
        if item != empty_char:
            yield item


def has_no_duplicates(enumerable):
    seen = set()
    for item in enumerable:
        if item in seen:
            return False
        seen.add(item)
    return True
