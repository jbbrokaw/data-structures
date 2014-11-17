from __future__ import unicode_literals
from bst import BST


class AVLTree(BST):
    def __init__(self):
        self._level = 0  # 1 at leaves, depth at head, 0 for empty tree
        BST.__init__(self)

    def balance(self):  # Overrides BST.balance()
        leftdepth = 0 if not self.leftchild else self.leftchild.depth()
        rightdepth = 0 if not self.rightchild else self.rightchild.depth()
        return leftdepth - rightdepth

    def depth(self):  # Override, just returns _level
        return self._level

    def _relevel(self):  # Set _level based on children (after insert/rotate)
        if self.leftchild:
            leftlevel = self.leftchild._level
        else:
            leftlevel = 0
        if self.rightchild:
            rightlevel = self.rightchild._level
        else:
            rightlevel = 0
        self._level = max(leftlevel, rightlevel) + 1

    def _rotate_right(self):
        # Rotate self.rightchild into self
        if self._EMPTY or (self.rightchild is None):
            raise ValueError("Attempt to rotate with missing nodes")
        new_leftchild = AVLTree()
        new_leftchild.insert(self.value)
        new_leftchild.leftchild = self.leftchild
        new_leftchild.rightchild = self.rightchild.leftchild
        new_leftchild._relevel()
        self.leftchild = new_leftchild
        self.value = self.rightchild.value
        self.rightchild = self.rightchild.rightchild
        self._relevel()

    def _rotate_left(self):
        # Rotate self.leftchild into self
        if self._EMPTY or (self.leftchild is None):
            raise ValueError("Attempt to rotate with missing nodes")
        new_rightchild = AVLTree()
        new_rightchild.insert(self.value)
        new_rightchild.rightchild = self.rightchild
        new_rightchild.leftchild = self.leftchild.rightchild
        new_rightchild._relevel()
        self.rightchild = new_rightchild
        self.value = self.leftchild.value
        self.leftchild = self.leftchild.leftchild
        self._relevel()

    def _rebalance(self):
        if self.balance() == 2:  # We're left-heavy, check if left-right
            if self.leftchild.balance() < 0:  # left-right
                self.leftchild._rotate_right()
            # now we're for sure left-left
            self._rotate_left()
            return
        if self.balance() == -2:  # We're right-heavy, check if right-left
            if self.rightchild.balance() > 0:  # right-left
                self.rightchild._rotate_left()
            self._rotate_right()
            return
        raise ValueError("Tree too unbalanced")

    def insert(self, val):
        """insert val into the AVLTree & rebalance. If val is already there,
        it is ignored."""
        if self._EMPTY:
            self.value = val
            self._EMPTY = False
            self._level = 1
            return

        if val == self.value:
            return

        if val > self.value:
            if not self.rightchild:
                self.rightchild = AVLTree()  # Make a subtree
            self.rightchild.insert(val)
            self._relevel()
            if self.balance() < -1:
                self._rebalance()
            return

        # If we get here it goes left
        if not self.leftchild:
            self.leftchild = AVLTree()  # Make a subtree
        self.leftchild.insert(val)
        self._relevel()
        if self.balance() > 1:
            self._rebalance()

    def _replacenode(self, newnode):  # Adding _level update
        BST._replacenode(self, newnode)
        self._relevel()

    def _find_minimum_and_delete(self, parent=None):
        """Return the minimum value of a (sub)tree and delete its node"""
        nodes_to_update = []
        if parent:
            nodes_to_update.append(parent)
        current = self
        while current.leftchild:
            nodes_to_update.append(current)
            parent = current
            current = current.leftchild
        returnval = current.value
        current.delete(current.value, parent)
        for node in reversed(nodes_to_update):
            node._relevel()
            if abs(node.balance()) > 1:
                node._rebalance()
        return returnval

    def _find_maximum_and_delete(self, parent=None):
        """Return the maximum value of a (sub)tree and delete its node"""
        nodes_to_update = []
        if parent:
            nodes_to_update.append(parent)
        current = self
        while current.rightchild:
            nodes_to_update.append(current)
            parent = current
            current = current.rightchild
        returnval = current.value
        current.delete(current.value, parent)
        for node in reversed(nodes_to_update):
            node._relevel()
            if abs(node.balance()) > 1:
                node._rebalance()
        return returnval

    def delete(self, val, parent=None):
        """Remove val from the tree if present. If not present no change.
        Rebalance if necessary. Return None in all cases"""
        if self._EMPTY:  # We're an empty head
            return
        if val == self.value:
            # Do the deletion
            if (not self.leftchild) and (not self.rightchild):
                if parent:
                    if parent.leftchild and (parent.leftchild is self):
                        parent.leftchild = None
                    else:  # We must be the right child
                        parent.rightchild = None
                    parent._relevel()
                    return
                # No parent (we are head) if we are here
                self.value = None
                self._EMPTY = True
                self._level = 0
                return

            # Here, we know we have at least one child
            if not self.leftchild:  # must have only a rightchild
                self._replacenode(self.rightchild)
                return
            if not self.rightchild:  # must have only a leftchild
                self._replacenode(self.leftchild)
                return

            # Here, we must do the two-child deletion
            if self.balance() < 0:  # left-heavy, delete on right
                self.value = \
                    self.rightchild._find_minimum_and_delete(parent=self)
            else:  # right-heavy (or balanced)
                self.value = \
                    self.leftchild._find_maximum_and_delete(parent=self)
            return

        # Keep searching (with parent info)
        if val > self.value:
            if not self.rightchild:
                return  # Val is not in tree
            self.rightchild.delete(val, parent=self)
            self._relevel()
            if abs(self.balance()) > 1:
                self._rebalance()
            return

        # If we get here it'll be on the left
        if not self.leftchild:
            return
        self.leftchild.delete(val, parent=self)
        if abs(self.balance()) > 1:
            self._rebalance()

if __name__ == '__main__':
    # Setup for visualization
    import random
    bintree = AVLTree()
    for i in xrange(100):
        bintree.insert(random.randint(0, 1e6))
    assert bintree.size() == 100
    bintree.update_dot()
    print "Balance = ", bintree.balance()
