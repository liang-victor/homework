"""145. Binary Tree Postorder Traversal

https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

from typing import List
from data_structures.binary_tree import TreeNode


def postorder_traversal(root: [TreeNode]) -> List[int]:
    if not root:
        return []

    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]
