"""101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

"""

from data_structures.binary_tree import TreeNode


def is_symmetric(root: TreeNode) -> bool:
    if not root:
        return True

    return traversal(root.left) == mirror_traversal(root.right)


def traversal(root):
    if not root:
        return [None]
    nodes_to_visit = [root]
    values = [root.val]

    while nodes_to_visit:
        next_nodes_to_visit = []
        for node in nodes_to_visit:
            if node.left:
                values.append(node.left.val)
                next_nodes_to_visit.append(node.left)
            else:
                values.append(None)
            if node.right:
                values.append(node.right.val)
                next_nodes_to_visit.append(node.right)
            else:
                values.append(None)

        nodes_to_visit = next_nodes_to_visit
    return values


def mirror_traversal(root):
    if not root:
        return [None]
    nodes_to_visit = [root]
    values = [root.val]

    while nodes_to_visit:
        next_nodes_to_visit = []
        for node in nodes_to_visit:
            if node.right:
                values.append(node.right.val)
                next_nodes_to_visit.append(node.right)
            else:
                values.append(None)
            if node.left:
                values.append(node.left.val)
                next_nodes_to_visit.append(node.left)
            else:
                values.append(None)

        nodes_to_visit = next_nodes_to_visit
    return values
