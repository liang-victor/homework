""" 226. Invert Binary Tree

    Given the root of a binary tree, invert the tree, and return its root.

    https://leetcode.com/problems/invert-binary-tree

"""

from data_structures.binary_tree import TreeNode
from collections import deque


def invert_tree(root):
    if not root:
        return None
    queue = deque()
    node = root
    queue.append(node)

    while queue:
        node = queue.popleft()

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp

    return root
