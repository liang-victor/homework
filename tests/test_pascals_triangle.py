import pytest
from pascals_triangle import generate


def test_1_row():
    assert generate(1) == [[1]]


def test_5_rows():
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
