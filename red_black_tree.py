from __future__ import unicode_literals
from bst import BST
BLACK = False
RED = True


class RedBlackTree(BST):
    def __init__(self):
        self.parent = None
        self.color = BLACK
        BST.__init__(self)

    def _preliminary_insert(self, val):
        """insert val into the BST (normally) and color it red"""
        if self._EMPTY:
            self.value = val
            self._EMPTY = False
            self.color = RED
            return

        if val == self.value:
            return

        if val > self.value:
            if not self.rightchild:
                self.rightchild = RedBlackTree()  # Make a subtree
            self.rightchild._preliminary_insert(val)
            return

        # If we get here it goes left
        if not self.leftchild:
            self.leftchild = RedBlackTree()  # Make a subtree
        self.leftchild._preliminary_insert(val)
        return