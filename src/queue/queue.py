from typing import Any
from typing import List


class CircularQueue:
    """A pretty inefficient circular queue implementation intended for study purposes only."""

    def __init__(self, size: int = None):
        self._data = list()
        self._size = size
        self._head = -1
        self._tail = -1

    def __bool__(self):
        return not self.is_empty()

    def __repr__(self):
        return (
            f"<CircularQueue object of size: "
            f"{self._size if self._size else 'undefined'}>"
        )

    def __len__(self):
        if self.is_empty():
            return 0
        return abs(self._tail - self._head + 1)

    def resize(self, size: int) -> List:
        """Resizes the queue.

        Returns:
            A list of elements removed after resizing.
        """

        # If there are more elements already, drop the rest.
        if self.__len__() > size:
            self._tail = size - 1
            copy = self._data[self._tail + 1:].copy()
            del self._data[self._tail + 1:]
            return copy

        self._size = size
        return []

    def is_empty(self) -> bool:
        return self._head == -1

    def is_full(self) -> bool:
        if not self._size:
            return False
        return (self._tail + 1) % self._size == self._head

    def front(self) -> Any:
        """Returns the first element in the queue."""

        if self.is_empty():
            return None
        return self._data[self._head]

    def back(self) -> Any:
        """Returns the last element in the queue."""

        if self.is_empty():
            return None
        return self._data[self._tail]

    def enqueue(self, elem) -> bool:
        """Adds a new element to the end of the queue.

        Returns:
            A boolean of whether operation was successful.
        """

        if self.is_full():
            return False

        # If inserting the first element.
        if self.is_empty():
            self._head = 0

        self._tail += 1
        if self._size:
            self._tail %= self._size

        self._data.insert(self._tail, elem)
        return True

    def dequeue(self) -> bool:
        """Removes the first element in the queue.

        Returns:
            A boolean of whether operation was successful.
        """

        if self.is_empty():
            return False

        # If removing the last element.
        if self._head == self._tail:
            self._head = -1
            self._tail = -1
            return True

        self._head += 1
        if self._size:
            self._head %= self._size

        return True
