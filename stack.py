from __future__ import unicode_literals


class Node(object):
    def __init__(self, content=None, next=None):
        self.content = content
        self.next = next


class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, data):
        if not self.top:
            self.top = Node(content=data)
        else:
            self.top = Node(content=data, next=self.top)

    def pop(self):
        if self.top:
            data = self.top.content
            self.top = self.top.next
            return data
        raise IndexError('pop from empty stack')
