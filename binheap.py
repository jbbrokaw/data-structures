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

    def _find_largest_child(self, index):
        """Find the index of the "largest" child of node index"""
        if 2 * index + 1 > self._bottom:
            return 2 * index + 1
        if 2 * index + 2 > self._bottom:
            return 2 * index + 1
        if self._compare(self._data[2 * index + 1], self._data[2 * index + 2]):
            return 2 * index + 1
        else:
            return 2 * index + 2

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
                and (current > 0):
            self._data[current], self._data[parent] = \
                self._data[parent], self._data[current]
            current = parent
            parent = self._find_parent(current)

    def pop(self):
        returnval = self._data[0]  # Will raise IndexError if empty
        if len(self._data) > 1:
            self._data[0] = self._data.pop()  # Put the last thing at the head
            self._bottom += -1
        else:
            self._data.pop()  # Remove the only item in there
            self._bottom += -1
            return returnval

        # Do a heap-down
        current = 0
        child = self._find_largest_child(current)
        while child <= self._bottom and \
                self._compare(self._data[child], self._data[current]):
            self._data[current], self._data[child] = \
                self._data[child], self._data[current]
            current = child
            child = self._find_largest_child(current)

        return returnval
