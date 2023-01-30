import pytest
from binary_tree_level_order_traversal import level_order
from data_structures.binary_tree import TreeNode


def test_level_order():
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e

    assert level_order(a) == [[3], [9, 20], [15, 7]]


def test_single_node():
    a = TreeNode(3)
    assert level_order(a) == [[3]]


def test_no_node():
    a = None

    assert level_order(a) == []
