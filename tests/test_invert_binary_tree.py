import pytest
from data_structures.binary_tree import TreeNode, level_order_traversal, construct_from_list
from invert_binary_tree import invert_tree


def test_example_1():
    input = [4, 2, 7, 1, 3, 6, 9]

    root = construct_from_list(input)

    invert_tree(root)
    assert level_order_traversal(root) == [[4], [7, 2], [9, 6, 3, 1]]
