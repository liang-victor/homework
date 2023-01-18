import pytest
from remove_duplicates_from_sorted_array import remove_duplicates


def check_values(nums, expected):
    for resulting_value, expected_value in zip(nums, expected):
        assert resulting_value == expected_value


def test_example_1():
    nums = [1, 1, 2]
    expected_k = 2
    expected = [1, 2]

    result = remove_duplicates(nums)

    assert result == expected_k
    check_values(nums, expected)


def test_example_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_k = 5
    expected = [0, 1, 2, 3, 4]

    result = remove_duplicates(nums)

    assert result == expected_k
    check_values(nums, expected)


def test_no_duplicates():
    nums = [0, 1, 2, 3]
    expected_k = 4
    expected = [0, 1, 2, 3]

    result = remove_duplicates(nums)

    assert result == expected_k
    check_values(nums, expected)


def test_empty():
    nums = []
    expected_k = 0
    expected = []

    result = remove_duplicates(nums)

    assert result == expected_k
    check_values(nums, expected)
