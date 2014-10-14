from __future__ import unicode_literals

from linked_list import LinkedList
from stack import Node


class DoubleNode(Node):
    def __init__(self, content=None, next=None, previous=None):
        self.previous = previous
        Node.__init__(self, content, next)


class DoublyLinkedList(LinkedList):
    # SOME NOTES on inheritance: print is backward (like a stack instead of a queue/list)
    # remove() is very different based on the spec.
    # search() was very helpful to inherit.
    top = None
    bottom = None

    def __init__(self):
        LinkedList.__init__(self)

    def insert(self, data):
        LinkedList.insert(self, data)  # This updates top, no previous needed on it
        if not self.bottom:  # There's nothing in the list!
            self.bottom = self.top  # This is the only thing, no previous or next
        else:  # There was other stuff in the list, the old top (top.next) needs a previous
            self.top.next.previous = self.top
        self.top.previous = None  # Need to define this attribute, since LinkedList.insert only makes a regular Node

    def push(self, data):
        self.insert(data)

    def append(self, data):
        if not self.bottom:  # Nothing in the list
            self.bottom = DoubleNode(data)
            self.top = self.bottom
        else:
            self.bottom.next = DoubleNode(data, next=None, previous=self.bottom)
            self.bottom = self.bottom.next

    def pop(self):
        val = LinkedList.pop(self)  # This will remove the top
        if self.top:  # If there's still something in the list
            self.top.previous = None  # We have to remove this
        else:  # Nothing in the list anymore
            self.bottom = None  # So we remove bottom, too
        return val

    def shift(self):
        if self.bottom:
            data = self.bottom.content
            self.bottom = self.bottom.previous
            if self.bottom:  # Still stuff in the list
                self.bottom.next = None
            else:  # Nothing in the list, update top
                self.top = None
            return data
        raise IndexError('pop from empty stack')

    def remove(self, value):
        node = self.search(value)
        if not node:
            raise IndexError('remove(node) where node was not in list')
        if node is self.top:
            self.top = self.top.next
            if self.top:
                self.top.previous = None
            else:  # the list is now empty
                self.bottom = None
                return None
        if node is self.bottom:  # list has at least 1 item after removal if we get here.
            self.bottom = self.bottom.previous
            self.bottom.next = None
            return None
        # It's in the middle if we get here, all this stuff should exist
        node.previous.next = node.next
        node.next.previous = node.previous
