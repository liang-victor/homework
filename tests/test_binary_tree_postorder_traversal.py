import pytest
from data_structures.binary_tree import TreeNode
from binary_tree_postorder_traversal import postorder_traversal


def test_postorder_traversal():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c

    assert postorder_traversal(a) == [3, 2, 1]


def test_empty_tree():
    a = None
    assert postorder_traversal(a) == []


def test_single_node():
    a = TreeNode(1)
    assert postorder_traversal(a) == [1]
