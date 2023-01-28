import pytest
from data_structures.binary_tree import TreeNode
from binary_tree_inorder_traversal import inorder_traversal


def test_inorder_traversal():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c

    assert inorder_traversal(a) == [1, 3, 2]


def test_empty_tree():
    a = None
    assert inorder_traversal(a) == []


def test_single_node():
    a = TreeNode(1)
    assert inorder_traversal(a) == [1]
