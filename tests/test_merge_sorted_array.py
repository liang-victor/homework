import pytest
from merge_sorted_array import merge


def test_example_1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    merge(nums1, m, nums2, n)

    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_example_2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0

    merge(nums1, m, nums2, n)

    assert nums1 == [1]


def test_example_3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1

    merge(nums1, m, nums2, n)

    assert nums1 == [1]


def test_run_out_of_num_2():
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1

    merge(nums1, m, nums2, n)

    assert nums1 == [1, 2]
