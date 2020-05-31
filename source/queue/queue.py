from collections import deque


class Queue:
    """
    I didn't want inefficient queue class based on python's lists,
    so I just wrapped the default deque container :\
    """

    def __init__(self, first=None, size=None):
        self.q = deque(maxlen=size)
        if first:
            self.enqueue(first)

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        return repr(self.q).replace('deque', 'queue')

    @property
    def is_empty(self):
        return not self.q

    @property
    def is_not_empty(self):
        return not self.is_empty

    def enqueue(self, element):
        self.q.append(element)

    def dequeue(self):
        if self.is_empty:
            return None
        return self.q.popleft()
