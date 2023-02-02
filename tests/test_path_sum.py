import pytest
from path_sum import has_path_sum
from data_structures.binary_tree import TreeNode, level_order_traversal, construct_from_list


def test_has_path_sum():
    root = construct_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    target = 22

    assert has_path_sum(root, target) is True


def test_simple_tree():
    root = construct_from_list([1, 2, 3])
    target = 5
    assert has_path_sum(root, target) is False


def test_empty():
    root = None
    target = 0
    assert has_path_sum(root, target) is False
