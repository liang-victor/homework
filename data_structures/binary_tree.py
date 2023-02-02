from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode: {self.val}. L: {self.left} R: {self.right}"


def construct_from_list(values):
    """Returns the root of a tree constructed from the listed values

    [1, 2, 3, 4, 5, 6, 7]

                            1
                        2       3
                      4   5   6   7
    """
    if not values:
        return None

    root = TreeNode(values[0])

    queue = deque()
    queue.append(root)
    i = 1

    while i < (len(values)):
        if i % 2 == 1:
            parent = queue.popleft()
            left = TreeNode(values[i])
            parent.left = left
            queue.append(left)
        else:
            right = TreeNode(values[i])
            parent.right = right
            queue.append(right)
        i += 1
    return root


def preorder_traversal(root: TreeNode) -> List[int]:
    if not root:
        return []

    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def level_order_traversal(root):
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
