from collections import deque


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'<Node: {type(self.value).__name__} = {self.value}>'

    def __bool__(self):
        return True

    def is_leaf(self):
        return not self.left and not self.right

    def children(self):
        for child in (self.left, self.right):
            yield child


class BinaryTree:

    def __init__(self):
        self._root = None

    def __bool__(self):
        return self._root is not None

    @property
    def root(self) -> Node:
        return self._root

    @root.setter
    def root(self, value):
        assert isinstance(value, Node)
        if self._root:
            raise AttributeError("Root value is already set.")
        self._root = value

    def preorder(self) -> list:

        def preorder_from(node):
            result = []
            if node:
                result.append(node.value)
                result += preorder_from(node.left)
                result += preorder_from(node.right)
            return result

        return preorder_from(self.root)

    def inorder(self) -> list:

        def inorder_from(node):
            result = []
            if node:
                result += inorder_from(node.left)
                result.append(node.value)
                result += inorder_from(node.right)
            return result

        return inorder_from(self.root)

    def postorder(self) -> list:

        def postorder_from(node):
            result = []
            if node:
                result += postorder_from(node.left)
                result += postorder_from(node.right)
                result.append(node.value)
            return result

        return postorder_from(self.root)

    def levelorder(self) -> list:
        if not self.root:
            return []

        # Queue for storing nodes to travers.
        queue = deque()
        queue.append([self.root])

        # List to store the traversed nodes' values.
        values = list()
        values.append([self.root.value])

        while queue:
            nodes = queue.popleft()
            subtrees = list()

            for node in nodes:
                if not node:
                    continue
                subtrees.extend(node.children())

            if not subtrees:
                continue

            queue.append(subtrees)

            level = [
                node.value if node else None
                for node in subtrees
            ]

            # Don't include the last level: [None, None, None, None]
            if any(level):
                values.append(level)

        return values

    def pretty(self) -> str:
        # Todo: implement me!
        pass


class BinarySearchTree(BinaryTree):

    def __init__(self):
        super().__init__()
        self._size = 0

    def __len__(self):
        return self._size

    def insert(self, value):
        if self.contains(value):
            return False

        def insert_at(node, value):
            if not node:
                return Node(value)

            if value < node.value:
                node.left = insert_at(node.left, value)

            if value > node.value:
                node.right = insert_at(node.right, value)

            return node

        self._root = insert_at(self.root, value)
        self._size += 1
        return True

    def remove(self, value, swap_rightmost=True):
        if not self.contains(value):
            return False

        def find_min(node):
            if not node.left:
                return node
            return find_min(node.left)

        def find_max(node):
            if not node.right:
                return node
            return find_max(node.right)

        def remove_at(node, value):
            # Case 1: If it contains value and at the same time has no children, we just replace it with `None`.
            if node.is_leaf:
                return None

            if value < node.value:
                node.left = remove_at(node.left, value)
                return node

            if value > node.value:
                node.right = remove_at(node.right, value)
                return node

            # value == node.value, then we can start trimming.
            # Case 2, 3: Only one subtree, then just replace with its child.
            if node.left and not node.right:
                return node.left

            if node.right and not node.left:
                return node.right

            # Case 4: Justify which child to replace with.
            # Actually it can be either the largest from the left subtree or the smallest from the right one.
            # We don't really care.
            replacement = find_min(node.right) if swap_rightmost else find_max(node.left)
            # That's cool, but now we need to delete this `replacement` node from the tree to avoid duplicate values.
            # Fortunately it will always be case 2, 3 node, since we went all the way down to the left to get it.
            # Hence, we won't get infinite recursion, so it's safe.
            node = remove_at(node, replacement.value)
            node.value = replacement.value
            return node

        self._root = remove_at(self._root, value)
        return True

    def find(self, value):

        def find_at(node, value):
            if not node:
                return None
            if value < node.value:
                return find_at(node.left, value)
            if value > node.value:
                return find_at(node.right, value)
            return node

        return find_at(self._root, value)

    def contains(self, value) -> bool:
        return self.find(value) is not None
