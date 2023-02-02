"""700. Search in a Binary Search Tree

https://leetcode.com/problems/search-in-a-binary-search-tre

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
"""
from typing import Optional
from data_structures.binary_tree import TreeNode


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None

    if root.val == val:
        return root
    elif root.val > val and root.left:
        return searchBST(root.left, val)
    elif root.val < val and root.right:
        return searchBST(root.right, val)
    else:
        return None
