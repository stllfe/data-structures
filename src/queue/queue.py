class CircularQueue:
    """A pretty inefficient circular queue implementation intended for study purposes only."""

    def __init__(self, size=None):
        self._data = list()
        self._size = size
        self._head = -1
        self._tail = -1

    def __bool__(self):
        return not self.is_empty()

    def __repr__(self):
        return (f"<{self.__class__.__name__} object of size: "
                f"{self._size if self._size else 'undefined'}>")

    def __len__(self):
        if self.is_empty():
            return 0
        return abs(self._tail - self._head + 1)

    def resize(self, size, drop=False):
        if not size:
            return False

        # If there are more elements already
        # drop the rest.
        if self.__len__() > size:
            self._tail = size - 1
            if drop:
                del self._data[self._tail + 1:]
                return True
            return self._data[self._tail + 1:]

        self._size = size
        return True

    def is_empty(self):
        return self._head == -1

    def is_full(self):
        if not self._size:
            return False
        return (self._tail + 1) % self._size == self._head

    def front(self):
        if self.is_empty():
            return None
        return self._data[self._head]

    def back(self):
        if self.is_empty():
            return None
        return self._data[self._tail]

    def enqueue(self, obj):
        if self.is_full():
            return False

        # If inserting the first element
        if self.is_empty():
            self._head = 0

        self._tail += 1
        if self._size:
            self._tail %= self._size

        self._data.insert(self._tail, obj)
        return True

    def dequeue(self):
        if self.is_empty():
            return False

        # If removing the last element
        if self._head == self._tail:
            self._head = -1
            self._tail = -1
            return True

        self._head += 1
        if self._size:
            self._head %= self._size

        return True
