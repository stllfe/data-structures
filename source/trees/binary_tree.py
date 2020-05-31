from source.queue import Queue


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @property
    def is_leaf(self):
        return not self.left and not self.right

    @property
    def children(self):
        children = list()
        for child in (self.left, self.right):
            if child:
                children.append(child)
        return children


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def _insert_at(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_at(node.left, value)

        if value > node.value:
            node.right = self._insert_at(node.right, value)

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
        # case 1: if it contains value and at the same time has no children, we just replace it with None
        if node.is_leaf:
            return None

        if value < node.value:
            node.left = self._remove_at(node.left, value)
            return node

        if value > node.value:
            node.right = self._remove_at(node.right, value)
            return node

        # value == node.value, then we can start trimming
        # case 2, 3: only one subtree, then just replace with its child
        if node.left and not node.right:
            return node.left

        if node.right and not node.left:
            return node.right

        # case 4: justify which child to replace with
        # actually it can be either the largest from the left subtree or the smallest from the right one
        # we don't really care, so let's do the latter
        replacement = self._find_min(node.right)
        # that's cool, but now we need to delete this `replacement` node from the tree to avoid duplicate values
        # fortunately it will always be case 2, 3 node, since we went all the way down to the left to get it
        # hence, we won't get infinite recursion, so it's safe
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

        self.root = self._insert_at(self.root, value)
        return True

    def remove(self, value):
        if not self.contains(value):
            return False

        self.root = self._remove_at(self.root, value)
        return True

    def find(self, value):
        return self._find_at(self.root, value)

    def contains(self, value):
        return self.find(value) is not None

    def preorder(self):
        return self._preorder_from(self.root)

    def inorder(self):
        return self._inorder_from(self.root)

    def postorder(self):
        return self._postorder_from(self.root)

    def level_order(self):
        if not self.root:
            return

        levels = list()
        q = Queue(first=[self.root])
        levels.append([self.root.value])

        while q.is_not_empty:
            nodes = q.dequeue()
            level = list()
            children = list()
            for node in nodes:
                children.extend(node.children)
                for child in node.children:
                    level.append(child.value)

            if not children:
                break

            q.enqueue(children)
            levels.append(level)

        return levels

    def print(self):
        # todo: implement me
        levels = self.level_order()
        for level in levels:
            pass


