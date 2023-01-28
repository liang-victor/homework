"""94. Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

"""

from typing import List
from data_structures.binary_tree import TreeNode


def inorder_traversal(root: [TreeNode]) -> List[int]:
    if not root:
        return []

    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
