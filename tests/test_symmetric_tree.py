import pytest
from data_structures.binary_tree import TreeNode
from symmetric_tree import is_symmetric


def test_example_1():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(4)
    g = TreeNode(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    assert is_symmetric(a) == True


def test_example_2():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(3)

    a.left = b
    a.right = c
    b.right = d
    c.right = e

    assert is_symmetric(a) == False


def test_example_3():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(4)
    g = TreeNode(2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    assert is_symmetric(a) == False
