import pytest
from search_2d_matrix import search_matrix, binary_search_rows


def test_trivial_matrix():
    matrix = [[1]]
    assert search_matrix(matrix, 1) == True

    assert search_matrix(matrix, 2) == False


def test_target_in_matrix():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert search_matrix(matrix, target) == True


def test_target_not_in_matrix():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert search_matrix(matrix, target) == False


def test_binary_search_rows_exact_match():
    matrix = [[2 * x] for x in range(200)]
    target = 50

    assert binary_search_rows(matrix, target) == True


def test_binary_search_rows_returns_row_index():
    matrix = [[2 * x] for x in range(200)]
    target = 51

    assert binary_search_rows(matrix, target) == 25


def test_binary_search_rows_outside_range():
    matrix = [[x + 25] for x in range(100)]

    assert binary_search_rows(matrix, 1) == False
    assert binary_search_rows(matrix, 300) == False
