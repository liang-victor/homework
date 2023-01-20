from maximum_subarray import max_subarray
import pytest


def test_single_value():
    nums = [1]
    assert max_subarray(nums) == 1


def test_all_positives():
    nums = [1, 2, 3]
    assert max_subarray(nums) == 6


def test_all_negative():
    nums = [-1, -2, -3]
    assert max_subarray(nums) == -1


def test_mixed_signs_full_array():
    nums = [5, 4, -1, 7, 8]
    assert max_subarray(nums) == 23


def test_take_the_left_side():
    nums = [5, -7, 1]
    assert max_subarray(nums) == 5


def test_take_the_right_side():
    nums = [5, -7, 10]
    assert max_subarray(nums) == 10


def test_multiple_negatives_in_a_row():
    nums = [5, -3, -4, 1]
    assert max_subarray(nums) == 5


def test_mixed_signs_sub_array():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray(nums) == 6


def test_mixed_signs_sub_array_2():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 8]
    assert max_subarray(nums) == 9


def test_positive_sequence_with_zero():
    nums = [2, -3, 0, 3]
    assert max_subarray(nums) == 3


def test_skip_sequences_containing_zero():
    nums = [1, -3, 2, 0, -1, 0, -2, -3, 1, 2, -3, 2]
    assert max_subarray(nums) == 3
