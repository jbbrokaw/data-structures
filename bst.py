from __future__ import unicode_literals
import random


class BST(object):
    # Will have attributes leftchild, rightchild, and value,
    # but they are ONLY added when needed
    def __init__(self):
        pass

    def insert(self, val):
        """insert val into the BST. If val is already there, it is ignored."""
        if not hasattr(self, "value"):
            self.value = val
            return

        if val == self.value:
            return

        if val > self.value:
            if not hasattr(self, "rightchild"):
                self.rightchild = BST()  # Make a subtree
            self.rightchild.insert(val)
            return

        # If we get here it goes left
        if not hasattr(self, "leftchild"):
            self.leftchild = BST()  # Make a subtree
        self.leftchild.insert(val)
        return

    def contains(self, val):
        """return True if val is in the BST, False if not."""
        if not hasattr(self, "value"):  # We're an empty head
            return False
        if val == self.value:
            return True
        if val > self.value:
            if not hasattr(self, "rightchild"):
                return False
            return self.rightchild.contains(val)

        # If we get here it'll be on the left
        if not hasattr(self, "leftchild"):
            return False
        return self.leftchild.contains(val)

    def size(self):
        """return the integer size of the BST (total number of values stored)
        0 if the tree is empty."""
        if not hasattr(self, "value"):  # We're an empty head
            return 0

        if not hasattr(self, "rightchild"):
            rightsize = 0
        else:
            rightsize = self.rightchild.size()

        if not hasattr(self, "leftchild"):
            leftsize = 0
        else:
            leftsize = self.leftchild.size()

        return rightsize + leftsize + 1  # Self plus all children

    def depth(self):
        """return an integer representing the total number of levels in the
        tree."""
        if not hasattr(self, "value"):  # We're an empty head
            return 0

        if not hasattr(self, "rightchild"):
            rightdepth = 0
        else:
            rightdepth = self.rightchild.depth()

        if not hasattr(self, "leftchild"):
            leftdepth = 0
        else:
            leftdepth = self.leftchild.depth()

        return 1 + max(leftdepth, rightdepth)  # self plus deepest child

    def balance(self):
        """return a positive or negative integer that represents how well
        balanced the tree is. Trees deeper on the left return a positive values
        trees deeper on the right than the left return a negative value."""
        if not hasattr(self, "value"):  # We're an empty head
            return 0

        if not hasattr(self, "rightchild"):
            rightdepth = 0
        else:
            rightdepth = self.rightchild.depth()

        if not hasattr(self, "leftchild"):
            leftdepth = 0
        else:
            leftdepth = self.leftchild.depth()

        return leftdepth - rightdepth

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if not hasattr(self, "value")
                                       else ("\t%s;\n%s\n" % (
                                                    self.value,
                                                    "\n".join(self._get_dot())
                                                    )
                                            )
                                    )

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if hasattr(self, "leftchild"):
            yield "\t%s -> %s;" % (self.value, self.leftchild.value)
            for i in self.leftchild._get_dot():
                yield i
        elif hasattr(self, "rightchild"):
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if hasattr(self, "rightchild"):
            yield "\t%s -> %s;" % (self.value, self.rightchild.value)
            for i in self.rightchild._get_dot():
                yield i
        elif hasattr(self, "leftchild"):
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
