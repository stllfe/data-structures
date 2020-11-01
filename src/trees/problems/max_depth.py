from src.trees import BinaryTree
from src.trees.binary_tree import Node


def max_depth(tree: BinaryTree, top_down=True) -> int:
    """Given a binary tree, finds its maximum depth.

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

    Args:
        top_down (bool): Whether to solve using top-down approach (preorder) or bottom-up instead (postorder).
    """

    def top_down_solution(node: Node, current_depth: int):
        if not node:
            return 0
        current_depth += 1
        left_depth = top_down_solution(node.left, current_depth) if node.left else 0
        right_depth = top_down_solution(node.right, current_depth) if node.right else 0
        return max(current_depth, left_depth, right_depth)

    def bottom_up_solution(node: Node):
        if not node:
            return 0
        left_depth = bottom_up_solution(node.left)
        right_depth = bottom_up_solution(node.right)
        return max(left_depth, right_depth) + 1

    if top_down:
        return top_down_solution(tree.root, 0)

    return bottom_up_solution(tree.root)


