import pytest
from reshape_the_matrix import matrix_reshape


def test_expect_horizontal_vector():
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4

    expected = [[1, 2, 3, 4]]
    assert matrix_reshape(mat, r, c) == expected


def test_expect_vertical_vector():
    mat = [[1, 2], [3, 4]]
    r = 4
    c = 1

    expected = [[1], [2], [3], [4]]
    assert matrix_reshape(mat, r, c) == expected


def test_invalid_input():
    mat = [[1, 2], [3, 4]]
    r = 2
    c = 4

    expected = [[1, 2], [3, 4]]
    assert matrix_reshape(mat, r, c) == expected


def test_example_3():
    mat = [[1, 2], [3, 4], [5, 6]]
    r = 2
    c = 3

    expected = [[1, 2, 3], [4, 5, 6]]
    assert matrix_reshape(mat, r, c) == expected
