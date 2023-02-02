"""112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

https://leetcode.com/problems/path-sum/

"""

from data_structures.binary_tree import TreeNode
from typing import Optional


def has_path_sum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    running_sum = 0
    to_process = [(root, running_sum)]

    while to_process:
        current_node, running_sum = to_process.pop()
        running_sum += current_node.val

        if current_node.right:
            to_process.append((current_node.right, running_sum))
        if current_node.left:
            to_process.append((current_node.left, running_sum))

        is_leaf_node = current_node.left is None and current_node.right is None
        if is_leaf_node and running_sum == targetSum:
            return True

    return False
