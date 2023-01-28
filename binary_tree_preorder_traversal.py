"""144. Binary Tree Preorder Traversal

https://leetcode.com/problems/binary-tree-preorder-traversal/

Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

from data_structures.binary_tree import TreeNode
from typing import List


def preorder_traversal(root: TreeNode) -> List[int]:
    if not root:
        return []

    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)
