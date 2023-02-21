from collections import deque


class PeekingIterator:

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.queue = deque()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if len(self.queue) == 0:
            self.queue.append(self.iter.next())
        return self.queue[0]

    def next(self):
        """
        :rtype: int
        """
        if len(self.queue) == 0:
            self.queue.append(self.iter.next())
        return self.queue.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0 or self.iter.hasNext()
