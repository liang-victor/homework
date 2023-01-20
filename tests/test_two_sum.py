import pytest
from two_sum import two_sum


def test_two_sum_example_1():
    nums = [2, 7, 11, 15]
    target = 9

    assert two_sum(nums, target) == [0, 1]


def test_two_sum_example_2():
    nums = [3, 2, 4]
    target = 6

    assert two_sum(nums, target) == [1, 2]


def test_contains_duplicates():
    nums = [3, 3]
    target = 6

    assert two_sum(nums, target) == [0, 1]


def test_no_doubling_up():
    nums = [1, 3, 4, 2]
    target = 6
    assert two_sum(nums, target) == [2, 3]
