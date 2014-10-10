from __future__ import unicode_literals

from stack import Stack
import sys

class Linked_list(Stack):
    def __init__(self):
        Stack.__init__(self)

    def insert(self, data):
        Stack.push(self, data)
        #JBB: I could override push to make it not work anymore on Linked_lists (force users to call it insert), but eeeeeh.

    def size(self):
        s = 0
        node = self.top
        while node:
            s += 1
            node = node.next
        return s

    def search(self, val):
        if not self.top:
            return None
        node = self.top
        while node.content != val:
            node = node.next
            if not node:
                break
        return node

    def remove(self, node):
        if node is self.top:
            self.top = self.top.next
            return
        testnode = self.top
        while testnode.next is not node:
            if not testnode.next:
                raise IndexError('remove(node) where node was not in list')
            testnode = testnode.next
        # Now testnode is the one before node
        testnode.next = node.next

    def printll(self):
        sys.stdout.write("(")  # Have to use this because 'print X,' inserts spaces
        reversedStack = Stack()  # gotta print from bottom up, so we reverse it in this stack
        node = self.top
        while node:
            reversedStack.push(node.content)
            node = node.next

        while reversedStack.top:
            thing = reversedStack.pop()
            if isinstance(thing, unicode) or isinstance(thing, str):
                sys.stdout.write("'" + thing + "'")
            else:
                sys.stdout.write(str(thing))
            if reversedStack.top:
                sys.stdout.write(", ")
        sys.stdout.write(")")
