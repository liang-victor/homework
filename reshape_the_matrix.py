"""566. Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/?envType=study-plan&id=data-structure-i

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.


"""


def matrix_reshape(mat, r, c):
    if not valid_arguments(mat, r, c):
        return mat
    else:
        matrix_values = values(mat)
        result = []
        for i in range(r):
            result.append([next(matrix_values) for _ in range(c)])
        return result


def values(matrix):
    """returns a generator that yields the values from the matrix
    """
    for row in matrix:
        for value in row:
            yield value


def valid_arguments(mat, r, c):
    matrix_rows = len(mat)
    matrix_cols = len(mat[0])

    return matrix_rows * matrix_cols == r * c
