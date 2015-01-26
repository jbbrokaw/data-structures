from __future__ import unicode_literals


class BST(object):
    # To have an empty BST, we need to perhaps not have a "value"
    # but I want to be able to put "None" in this data structure
    # So I am using an "_EMPTY" boolean to denote that "value" should be
    # considered empty (and not full with None)
    def __init__(self):
        self.leftchild = None
        self.rightchild = None
        self._EMPTY = True  # Should only ever be true for the head node!
        self.value = None

    def insert(self, val):
        """insert val into the BST. If val is already there, it is ignored."""
        if self._EMPTY:
            self.value = val
            self._EMPTY = False
            return

        if val == self.value:
            return

        if val > self.value:
            if not self.rightchild:
                self.rightchild = BST()  # Make a subtree
            self.rightchild.insert(val)
            return

        # If we get here it goes left
        if not self.leftchild:
            self.leftchild = BST()  # Make a subtree
        self.leftchild.insert(val)
        return

    def contains(self, val):
        """return True if val is in the BST, False if not."""
        if self._EMPTY:  # We're an empty head
            return False
        if val == self.value:
            return True
        if val > self.value:
            if not self.rightchild:
                return False
            return self.rightchild.contains(val)

        # If we get here it'll be on the left
        if not self.leftchild:
            return False
        return self.leftchild.contains(val)

    def size(self):
        """return the integer size of the BST (total number of values stored)
        0 if the tree is empty."""
        if self._EMPTY:  # We're an empty head
            return 0

        if not self.rightchild:
            rightsize = 0
        else:
            rightsize = self.rightchild.size()

        if not self.leftchild:
            leftsize = 0
        else:
            leftsize = self.leftchild.size()

        return rightsize + leftsize + 1  # Self plus all children

    def depth(self):
        """return an integer representing the total number of levels in the
        tree."""
        if self._EMPTY:  # We're an empty head
            return 0

        if not self.rightchild:
            rightdepth = 0
        else:
            rightdepth = self.rightchild.depth()

        if not self.leftchild:
            leftdepth = 0
        else:
            leftdepth = self.leftchild.depth()

        return 1 + max(leftdepth, rightdepth)  # self plus deepest child

    def balance(self):
        """return a positive or negative integer that represents how well
        balanced the tree is. Trees deeper on the left return a positive values
        trees deeper on the right than the left return a negative value."""
        # Possibly worthwhile to keep this as a property and update it when
        # we insert/delete, rather than visit every node every time we call
        # this function
        if self._EMPTY:  # We're an empty head
            return 0

        if not self.rightchild:
            rightdepth = 0
        else:
            rightdepth = self.rightchild.depth()

        if not self.leftchild:
            leftdepth = 0
        else:
            leftdepth = self.leftchild.depth()

        return leftdepth - rightdepth

    def _find_minimum_and_delete(self, parent=None):
        """Return the minimum value of a (sub)tree and delete its node"""
        current = self  # Could update "self" in the loop but that's confusing
        while current.leftchild:
            parent = current
            current = current.leftchild
        returnval = current.value
        current.delete(current.value, parent)
        return returnval

    def _find_maximum_and_delete(self, parent=None):
        """Return the maximum value of a (sub)tree and delete its node"""
        # This is slightly repetitive with _find_minimum, but it's hard to
        # implement a min/max switch elegantly; I'll just repeat these 7 lines
        current = self
        while current.rightchild:
            parent = current
            current = current.rightchild
        returnval = current.value
        current.delete(current.value, parent)
        return returnval

    def _replacenode(self, newnode):
        # Basically self = newnode,
        # but that does't work in methods called on self
        # (just changes local name)
        self.value = newnode.value
        if newnode.leftchild:
            self.leftchild = newnode.leftchild
        elif self.leftchild:
            self.leftchild = None
        if newnode.rightchild:
            self.rightchild = newnode.rightchild
        elif self.rightchild:
            self.rightchild = None

    def delete(self, val, parent=None):
        """remove val from the tree if present. If not present no change.
        Return None in all cases"""
        if self._EMPTY:  # We're an empty head
            return
        if val == self.value:
            # Do the deletion
            if (not self.leftchild) and \
                    (not self.rightchild):
                if parent:
                    if parent.leftchild and parent.leftchild is self:
                        parent.leftchild = None
                    else:  # We must be the right child
                        parent.rightchild = None
                    return
                #No parent (we are head) if we are here
                self.value = None
                self._EMPTY = True
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
            return self.rightchild.delete(val, parent=self)

        # If we get here it'll be on the left
        if not self.leftchild:
            return
        return self.leftchild.delete(val, parent=self)

    def in_order(self):
        if self.leftchild:
            for i in self.leftchild.in_order():
                yield i

        if not self._EMPTY:
            yield self.value

        if self.rightchild:
            for i in self.rightchild.in_order():
                yield i

    def pre_order(self):
        if not self._EMPTY:
            yield self.value

        if self.leftchild:
            for i in self.leftchild.pre_order():
                yield i

        if self.rightchild:
            for i in self.rightchild.pre_order():
                yield i

    def post_order(self):
        if self.leftchild:
            for i in self.leftchild.post_order():
                yield i

        if self.rightchild:
            for i in self.rightchild.post_order():
                yield i

        if not self._EMPTY:
            yield self.value

    def _gen_level(self, level):
        if self._EMPTY:  # Empty generator for empty tree
            return
        if level == 0:  # We're on this level
            yield self.value
        elif level > 0:  # We're on a lower level
            if self.leftchild:
                for val in self.leftchild._gen_level(level - 1):
                    yield val
            if self.rightchild:
                for val in self.rightchild._gen_level(level - 1):
                    yield val

    def breadth_first(self):
        for level in xrange(self.depth()):
            for val in self._gen_level(level):
                yield val

    def _rebalance(self, parent=None):
        # Since deletion is done so as to help preserve balance,
        # delete & reinsert until we're good
        bal = self.balance()
        if abs(bal) > 1:
            val = self.value
            self.delete(val, parent)
            return val
        val = None
        if self.leftchild:
            val = self.leftchild._rebalance(parent=self)
        if (val is None) and self.rightchild:
            val = self.rightchild._rebalance(parent=self)
        return val

    def rebalance(self):
        deleted_value = self._rebalance()
        while deleted_value is not None:
            self.insert(deleted_value)
            deleted_value = self._rebalance()

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" \
            % (
                "" if self._EMPTY
                else ("\t%s;\n%s\n" % (self.value, "\n".join(self._get_dot())))
            )

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        import random
        if self.leftchild:
            yield "\t%s -> %s;" % (self.value, self.leftchild.value)
            for i in self.leftchild._get_dot():
                yield i
        elif self.rightchild:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.rightchild:
            yield "\t%s -> %s;" % (self.value, self.rightchild.value)
            for i in self.rightchild._get_dot():
                yield i
        elif self.leftchild:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)

    def update_dot(self):
        import io
        dotfile = io.open("test.dot", "w")
        dotfile.write(self.get_dot())
        dotfile.close()


if __name__ == '__main__':
    import random
    # Setup for visualization
    bintree = BST()
    for i in xrange(50):
        bintree.insert(random.randint(0, 1e4))
    assert bintree.size() == 50
    bintree.update_dot()
    print "Balance = ", bintree.balance()
