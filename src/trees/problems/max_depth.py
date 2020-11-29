r"""Given a binary tree, finds its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Note:
        A leaf is a node with no children.

    Example:
        Given binary tree [3,9,20,null,null,15,7]
            3
           / \
          9  20
            /  \
           15   7
        Returns its depth = 3
"""

from src.trees import BinaryTree
from src.trees.binary_tree import Node


def max_depth_recursively(tree: BinaryTree, top_down=True) -> int:
    """Solves the problem recursively.

    Args:
        tree (BinaryTree): The tree to find max depth of.
        top_down (bool): Whether to solve using top-down (preorder) approach or bottom-up (postorder) instead.
    """

    def top_down_approach(node: Node, curr_depth: int):
        if not node:
            return 0
        curr_depth += 1
        left_depth = top_down_approach(node.left, curr_depth)
        right_depth = top_down_approach(node.right, curr_depth)
        return max(curr_depth, left_depth, right_depth)

    def bottom_up_approach(node: Node):
        if not node:
            return 0
        left_depth = bottom_up_approach(node.left)
        right_depth = bottom_up_approach(node.right)
        return max(left_depth, right_depth) + 1

    if top_down:
        return top_down_approach(tree.root, 0)
    return bottom_up_approach(tree.root)


