r"""Given a binary tree, check whether it is a mirror of itself (i. e., symmetric around its center).

        Example:
               1
              / \
             2   2
            / \ / \
           3  4 4  3
        This binary tree [1,2,2,3,4,4,3] is symmetric.
"""

from collections import deque

from src.trees import BinaryTree
from src.trees.binary_tree import Node


def is_symmetric_iteratively(tree: BinaryTree) -> bool:
    """Solves the problem iteratively.

    Intuition:
        Travers the tree level by level, validating that level's values array is mirrored.
        It's pretty much the same as level-order traversal except we have to handle null values carefully.

    Complexity:
        O(n) space and time, where n is the total number of nodes in the tree.
    """

    def is_mirrored_level(level):
        num_children = len(level)
        mid_idx = num_children // 2
        left, right = level[:mid_idx], level[mid_idx:]

        if left != right[::-1]:
            return False

        return True

    queue = deque()
    queue.append([tree.root])
    while queue:
        nodes = queue.popleft()
        subtrees = [child for node in nodes if node for child in node.children()]

        if not subtrees:
            continue
        if not is_mirrored_level([node.value if node else None for node in subtrees]):
            return False

        queue.append(subtrees)
    return True


def is_symmetric_recursively(tree: BinaryTree) -> bool:
    """Solves the problem recursively.

    Intuition:
        A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
        Therefore, the question is: when are two trees a mirror reflection of each other?

    Two trees are a mirror reflection of each other if:
        1. Their two roots have the same value.
        2. The right subtree of each tree is a mirror reflection of the left subtree of the other tree.

    Complexity:
        O(n) space and time, where n is the total number of nodes in the tree.
    """

    def is_mirrored_subtrees(n1: Node, n2: Node):
        if n1 is n2 is None:
            return True
        if not n1 or not n2:
            return False
        return (
                n1.value == n2.value and
                is_mirrored_subtrees(n1.left, n2.right) and
                is_mirrored_subtrees(n1.right, n2.left)
        )

    if not tree.root:
        return True

    return is_mirrored_subtrees(tree.root.left, tree.root.right)
