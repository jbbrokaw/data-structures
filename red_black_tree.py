from __future__ import unicode_literals
from bst import BST
BLACK = False
RED = True


class RedBlackTree(BST):
    def __init__(self):
        self.parent = None
        self.color = BLACK
        BST.__init__(self)

    def insert(self, val, parent=None):
        """insert val into the BST (normally) and color it red"""
        if self._EMPTY:
            self.value = val
            self._EMPTY = False
            self.parent = parent
            if self.parent:  # Otherwise it's the root & just stays black
                self.color = RED
                self._enforce_red_black_constraints()
            return

        if val == self.value:
            return

        if val > self.value:
            if not self.rightchild:
                self.rightchild = RedBlackTree()  # Make a subtree
            self.rightchild.insert(val, parent=self)
            return

        # If we get here it goes left
        if not self.leftchild:
            self.leftchild = RedBlackTree()  # Make a subtree
        self.leftchild.insert(val, parent=self)
        return

    def _grandparent(self):
        """Return the grandparent of this node, or None if doesn't exist"""
        if self.parent:
            return self.parent.parent
        return None

    def _enforce_red_black_constraints(self):
        """Determine which case we are in and repaint/rotate accordingly"""
        pass
