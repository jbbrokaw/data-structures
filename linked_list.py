from __future__ import unicode_literals
from stack import Stack


class Node(object):
    def __init__(self, content=None, next=None):
        self.content = content
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(content=data)
        else:
            self.head = Node(content=data, next=self.head)

    def size(self):
        s = 0
        node = self.head
        while node:
            s += 1
            node = node.next
        return s

    def search(self, value):
        if not self.head:
            return None
        node = self.head
        while node.content != value:
            node = node.next
            if not node:
                break
        return node

    def remove(self, node):
        if node is self.head:
            self.head = self.head.next
            return
        testnode = self.head
        while testnode.next is not node:
            if not testnode.next:
                raise IndexError('remove(node) where node was not in list')
            testnode = testnode.next
        # Now testnode is the one before node
        testnode.next = node.next

    def pop(self):
        if self.head:
            data = self.head.content
            self.head = self.head.next
            return data
        raise IndexError('pop from empty stack')

    def __str__(self):
        outstring = "("
        reversedStack = Stack()  # gotta print from first in to last in,
        node = self.head         # so we reverse it in this stack
        while node:
            reversedStack.push(node.content)
            node = node.next

        while reversedStack.top:
            thing = reversedStack.pop()
            if isinstance(thing, unicode) or isinstance(thing, str):
                outstring += "'" + thing + "'"
            else:
                outstring += str(thing)
            if reversedStack.top:
                outstring += ", "
        outstring += ")"
        return outstring

    def printll(self):
        print self.__str__()
