from __future__ import unicode_literals


class Binheap(object):
    def __init__(self, itdata=[], prop="max"):

        if prop == "max":
            self._comp = 1
        elif prop == "min":
            self._comp = -1
        else:
            raise ValueError("prop must be 'min' or 'max'")

        self._data = []
        self._bottom = -1  # Index of the last thing filled; no data, so -1

        if itdata:
            for i in itdata:
                self.push(i)

    def _find_parent(self, index):
        return (index - 1) // 2

    def _find_child(self, index):
        """Find the index of the first child (second child is retrunval + 1)"""
        return 2 * index + 1

    def _compare(self, val1, val2):
        if self._comp == 1:
            return val1 > val2
        else:
            return val1 < val2

    def push(self, value):
        self._data.append(value)
        self._bottom += 1
        current = self._bottom
        parent = self._find_parent(current)
        while self._compare(self._data[current], self._data[parent]) \
                and current > 0:
            self._data[current], self._data[parent] = \
                self._data[parent], self._data[current]
            current = parent
            parent = self._find_parent(current)
