from collections import deque


class Node:

    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def __str__(self):
        return f"<Node ('{type(self._value).__name__}'): {self._value}>"

    def __bool__(self):
        return True

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def is_leaf(self):
        return not self._left and not self._right

    @property
    def children(self):
        return [child for child in (self._left, self._right) if child]


class BinarySearchTree:

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __bool__(self):
        return self._root is not None

    @property
    def root(self) -> Node:
        return self._root

    def _insert_at(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node._left = self._insert_at(node._left, value)

        if value > node.value:
            node._right = self._insert_at(node._right, value)

        return node

    def _find_at(self, node, value):
        if not node:
            return None

        if value < node.value:
            return self._find_at(node.left, value)

        if value > node.value:
            return self._find_at(node.right, value)

        return node

    def _remove_at(self, node, value):
        # Case 1: If it contains value and at the same time has no children, we just replace it with `None`.
        if node.is_leaf:
            return None

        if value < node.value:
            node.left = self._remove_at(node.left, value)
            return node

        if value > node.value:
            node.right = self._remove_at(node.right, value)
            return node

        # value == node.value, then we can start trimming.
        # Case 2, 3: Only one subtree, then just replace with its child.
        if node.left and not node.right:
            return node.left

        if node.right and not node.left:
            return node.right

        # Case 4: Justify which child to replace with.
        # Actually it can be either the largest from the left subtree or the smallest from the right one.
        # We don't really care, so let's do the latter.
        replacement = self._find_min(node.right)
        # That's cool, but now we need to delete this `replacement` node from the tree to avoid duplicate values.
        # Fortunately it will always be case 2, 3 node, since we went all the way down to the left to get it.
        # Hence, we won't get infinite recursion, so it's safe.
        node = self._remove_at(node, replacement.value)
        node.value = replacement.value
        return node

    def _find_min(self, node):
        if not node.left:
            return node

        return self._find_min(node.left)

    def _find_max(self, node):
        if not node.right:
            return node

        return self._find_max(node.right)

    def _preorder_from(self, node):
        result = []
        if node:
            result.append(node.value)
            result += self._preorder_from(node.left)
            result += self._preorder_from(node.right)
        return result

    def _inorder_from(self, node):
        result = []
        if node:
            result += self._inorder_from(node.left)
            result.append(node.value)
            result += self._inorder_from(node.right)
        return result

    def _postorder_from(self, node):
        result = []
        if node:
            result += self._postorder_from(node.left)
            result += self._postorder_from(node.right)
            result.append(node.value)
        return result

    def insert(self, value):
        if self.contains(value):
            return False

        self._root = self._insert_at(self._root, value)
        self._size += 1
        return True

    def remove(self, value):
        if not self.contains(value):
            return False

        self._root = self._remove_at(self._root, value)
        return True

    def find(self, value):
        return self._find_at(self._root, value)

    def contains(self, value) -> bool:
        return self.find(value) is not None

    def preorder(self) -> list:
        return self._preorder_from(self._root)

    def inorder(self) -> list:
        return self._inorder_from(self._root)

    def postorder(self) -> list:
        return self._postorder_from(self._root)

    def levelorder(self) -> list:
        if not self.root:
            return []

        levels = list()
        queue = deque()
        queue.append([self.root])

        levels.append([self.root.value])

        while queue:
            nodes = queue.popleft()
            level = list()
            children = list()
            for node in nodes:
                children.extend(node.children)
                for child in node.children:
                    level.append(child.value)
            if not children:
                break
            queue.append(children)
            levels.append(level)

        return levels

    def pretty(self) -> str:
        # Todo: implement me!
        pass
