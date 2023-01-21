import pytest
from intersection_of_two_arrays_ii import intersect


def test_example_1():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert intersect(nums1, nums2) == [2, 2]


def test_example_2():
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = intersect(nums1, nums2)
    assert result == [4, 9] or result == [9, 4]
