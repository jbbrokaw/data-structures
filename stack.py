from __future__ import unicode_literals


class Node(object):
    def __init__(self, content=None, next=None):
        self.content = content
        self.next = next


class Stack(object):
    top = None

    def __init__(self):
        pass

    def push(self, data):
        if not self.top:
            self.top = Node(data)
        else:
            self.top = Node(data, self.top)

    def pop(self):
        if self.top:
            data = self.top.content
            self.top = self.top.next
            return data
        raise IndexError('pop from empty stack')
