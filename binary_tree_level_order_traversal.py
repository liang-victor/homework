"""102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


def level_order(root):
    """
    Return the items as sub-lists from BFS

    For BFS, queue up child nodes to visit in each level
    """

    if root is None:
        return []

    result = [[root.val]]
    queue = [root]

    while len(queue) > 0:
        level = []
        for node in queue:
            if node.left is not None:
                level.append(node.left)
            if node.right is not None:
                level.append(node.right)
        if level:
            result.append([node.val for node in level])
        queue = level

    return result
