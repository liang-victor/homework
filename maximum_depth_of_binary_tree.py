"""104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

https://leetcode.com/problems/maximum-depth-of-binary-tree/?

"""
from data_structures.binary_tree import TreeNode


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    queue = [root]
    level = 0

    while queue:
        level += 1
        next_queue = []
        for node in queue:
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue

    return level
