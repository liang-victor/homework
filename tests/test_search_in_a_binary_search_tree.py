import pytest
from data_structures.binary_tree import construct_from_list, preorder_traversal
from search_in_a_binary_search_tree import searchBST


def test_search_bst():
    root = construct_from_list([4, 2, 7, 1, 3])
    result = searchBST(root, 2)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3


def test_search_bst():
    root = construct_from_list([4, 2, 7, 1, 3])
    result = searchBST(root, 5)
    assert result is None
