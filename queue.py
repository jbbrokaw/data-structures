from __future__ import unicode_literals

from doubly_linked_list import DoubleNode


class Queue(object):
    # Note thatDirections are back <- [next, value, previous] -> front
    # (i.e., the agent at the front of the line calls "NEXT" to get the
    # next customer)
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, data):
        if not self.back:
            self.front = self.back = DoubleNode(content=data,
                                                previous=None,
                                                next=None)
        else:
            self.back = DoubleNode(content=data, previous=self.back, next=None)
            self.back.previous.next = self.back

    def dequeue(self):
        if not self.front:
            raise IndexError("dequeue from empty queue")
        returndata = self.front.content
        self.front = self.front.next
        if self.front:  # The list is not empty now
            self.front.previous = None
        else:  # The list is empty, need to remove back pointer
            self.back = None
        return returndata

    def size(self):
        if not self.back:
            return 0
        size = 1
        node = self.back
        while node.previous:
            size += 1
            node = node.previous
        return size
