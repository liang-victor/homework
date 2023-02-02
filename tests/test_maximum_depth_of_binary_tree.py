import pytest
from maximum_depth_of_binary_tree import max_depth
from data_structures.binary_tree import TreeNode


def test_example_1():
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)

    a.left = b
    a.right = c
    c.left = d
    c.right = e

    assert max_depth(a) == 3


def test_example_2():
    a = TreeNode(1)
    b = TreeNode(2)

    a.right = b

    assert max_depth(a) == 2


def test_single_node():
    a = TreeNode(1)
    assert max_depth(a) == 1


def test_empty_node():
    a = None
    assert max_depth(a) == 0
