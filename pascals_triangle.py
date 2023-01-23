"""Pascal's Triangle

https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

My solution:

Let's use symmetry to help generate the rows of the triangle

row     result                      stack values
1       1                           1
2       1, 1                        1
3       1, 2, 1                     1, 2
4       1, 3, 3, 1                  1, 3
5       1, 4, 6, 4, 1               1, 4, 6
6       1, 5, 10, 10, 5, 1          1, 5, 10

- each row is the result of a stack of values + its reverse
- on even numbers the center value is doubled, on odd numbers it occurs once
- the first value in the stack is always 1
    - the stack gains additional values every 2 rows, on the odd row
    - we need one additional numbers on rows 3 and 4
    - 2 additional numbers on rows 5 and 6
"""


def generate(numRows):
    result = []
    prev_row = []
    for n in range(numRows):
        row_number = n + 1
        values = [1]

        for i in range(n // 2):
            values.append(prev_row[i] + prev_row[i + 1])

        if odd(row_number):
            row = values + list(reversed(values[:-1]))
        else:
            row = values + list(reversed(values))

        result.append(row)
        prev_row = row
    return result


def odd(number):
    return number % 2 != 0
