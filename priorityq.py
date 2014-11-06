from __future__ import unicode_literals

from binheap import Binheap


class PriorityQueue(Binheap):
    """Acts just like a binheap, but takes tuples of (priority, data) and
    heaps on priority"""
    def _compare(self, tuple1, tuple2):  # Override
        """Compare using Binheap's protocol explicitly on first value of tuple
        (this is actually python's default behavior, but it's nice to make it
        explicit)"""
        return Binheap._compare(self, tuple1[0], tuple2[0])

    def insert(self, item):
        """Make sure it's a tuple and try to insert it"""
        try:
            assert isinstance(item, tuple)
            assert len(item) == 2
        except AssertionError:
            raise ValueError("Only tuples of (priority, data) are valid")
        Binheap.push(self, item)

    def push(self, item):  # Overriding binheap's, using PriorityQ type check
        self.insert(item)

    def peek(self):
        """Return highest (or lowest, depending on prop) priority value
        without removing from the PriorityQueue"""
        return self._data[0][1]  # Raises IndexError if not there, as intended

    def pop(self):
        """Return highest priority value in queue (with attached priority)"""
        return Binheap.pop(self)
