import pytest
from data_structures.binary_tree import TreeNode
from binary_tree_preorder_traversal import preorder_traversal


def test_preorder_traversal():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.right = c

    assert preorder_traversal(a) == [1, 2, 3]


def test_empty_tree():
    a = None
    assert preorder_traversal(a) == []


def test_single_nod():
    a = TreeNode(1)
    assert preorder_traversal(a) == [1]
