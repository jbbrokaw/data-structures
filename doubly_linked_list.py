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

    def __init__(self):
        self.head = None
        self.tail = None
        LinkedList.__init__(self)

    def insert(self, data):
        LinkedList.insert(self, data)  # This updates head, no previous needed on it
        if not self.tail:  # There's nothing in the list!
            self.tail = self.head  # This is the only thing, no previous or next
        else:  # There was other stuff in the list, the old head (head.next) needs a previous
            self.head.next.previous = self.head
        self.head.previous = None  # Need to define this attribute, since LinkedList.insert only makes a regular Node

    def push(self, data):
        self.insert(data)

    def append(self, data):
        if not self.tail:  # Nothing in the list
            self.tail = DoubleNode(data)
            self.head = self.tail
        else:
            self.tail.next = DoubleNode(data, next=None, previous=self.tail)
            self.tail = self.tail.next

    def pop(self):
        val = LinkedList.pop(self)  # This will remove the head
        if self.head:  # If there's still something in the list
            self.head.previous = None  # We have to remove this
        else:  # Nothing in the list anymore
            self.tail = None  # So we remove tail, too
        return val

    def shift(self):
        if self.tail:
            data = self.tail.content
            self.tail = self.tail.previous
            if self.tail:  # Still stuff in the list
                self.tail.next = None
            else:  # Nothing in the list, update head
                self.head = None
            return data
        raise IndexError('pop from empty stack')

    def remove(self, value):
        node = self.search(value)
        if not node:
            raise IndexError('remove(node) where node was not in list')
        if node is self.head:
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            else:  # the list is now empty
                self.tail = None
                return None
        if node is self.tail:  # list has at least 1 item after removal if we get here.
            self.tail = self.tail.previous
            self.tail.next = None
            return None
        # It's in the middle if we get here, all this stuff should exist
        node.previous.next = node.next
        node.next.previous = node.previous
