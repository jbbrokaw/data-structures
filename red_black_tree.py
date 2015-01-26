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

    @property
    def grandparent(self):
        """Return the grandparent of this node, or None if doesn't exist"""
        if self.parent:
            return self.parent.parent
        return None

    @property
    def uncle(self):
        """Return the uncle node, or None if it doesn't exist"""
        if self.grandparent is None:
            return None
        if self.parent is self.grandparent.leftchild:
            return self.grandparent.rightchild
        return self.grandparent.leftchild

    @property
    def sibling(self):
        """Return sibling node, None if it doesn't exist"""
        if self.parent:
            if self is self.parent.leftchild:
                return self.parent.rightchild
            else:
                return self.parent.leftchild
        return None

    def _rotate_right(self):
        # Rotate self.rightchild into self
        if self._EMPTY or (self.rightchild is None):
            raise ValueError("Attempt to rotate with missing nodes")
        new_leftchild = RedBlackTree()
        new_leftchild.insert(self.value)
        new_leftchild.color = self.color

        new_leftchild.leftchild = self.leftchild
        if new_leftchild.leftchild is not None:
            new_leftchild.leftchild.parent = new_leftchild

        new_leftchild.rightchild = self.rightchild.leftchild
        if new_leftchild.rightchild is not None:
            new_leftchild.rightchild.parent = new_leftchild

        self.leftchild = new_leftchild
        new_leftchild.parent = self

        self.value = self.rightchild.value
        self.color = self.rightchild.color

        self.rightchild = self.rightchild.rightchild
        if self.rightchild is not None:
            self.rightchild.parent = self

    def _rotate_left(self):
        # Rotate self.leftchild into self
        if self._EMPTY or (self.leftchild is None):
            raise ValueError("Attempt to rotate with missing nodes")
        new_rightchild = RedBlackTree()
        new_rightchild.insert(self.value)
        new_rightchild.color = self.color

        new_rightchild.rightchild = self.rightchild
        if new_rightchild.rightchild is not None:
            new_rightchild.rightchild.parent = new_rightchild

        new_rightchild.leftchild = self.leftchild.rightchild
        if new_rightchild.leftchild is not None:
            new_rightchild.leftchild.parent = new_rightchild

        self.rightchild = new_rightchild
        new_rightchild.parent = self

        self.value = self.leftchild.value
        self.color = self.leftchild.color

        self.leftchild = self.leftchild.leftchild
        if self.leftchild is not None:
            self.leftchild.parent = self

    def _enforce_red_black_constraints(self):
        """Determine which case we are in and repaint/rotate accordingly"""
        if self.parent is None:
            # We are the root, CASE 1
            self.color = BLACK
            return

        if self.parent.color is BLACK:
            # Everything is fine, CASE 2
            return

        if (self.parent.color is RED) and ((self.uncle is not None) and
                                           (self.uncle.color is RED)):
            # Repaint parent & uncle, fix grandparent, CASE 3
            self.parent.color = BLACK
            if self.uncle:
                self.uncle.color = BLACK
            self.grandparent.color = RED
            self.grandparent._enforce_red_black_constraints()
            return

        if ((self.grandparent.leftchild is not None) and
                (self is self.grandparent.leftchild.rightchild)):
            # We know our parent is RED, uncle must be BLACK, CASE 4A
            self.parent._rotate_right()  # Rotate self into parent
            # Now "self" refers to invalid orphan node, we want
            # self.parent.leftchild for CASE 5
            self = self.parent.leftchild
        elif ((self.grandparent.rightchild is not None) and
              (self is self.grandparent.rightchild.leftchild)):
            # The other option, CASE 4B
            self.parent._rotate_left()  # Rotate self into parent
            # Now "self" refers to invalid orphan node, we want
            # self.parent.rightchild for CASE 5
            self = self.parent.rightchild

        # CASE 5, parent is red, uncle black, we are
        # left/left or right/right from grandparent
        self.parent.color = BLACK
        self.grandparent.color = RED
        if ((self.grandparent.rightchild is not None) and
                (self.parent is self.grandparent.rightchild)):
            self.grandparent._rotate_right()
        else:
            self.grandparent._rotate_left()

    def delete(self, val, parent=None):
        """remove val from the tree if present. If not present no change.
        Return None in all cases. Rebalance according to red-black rules"""
        if self._EMPTY:  # We're an empty head
            return
        if val == self.value:
            # Do the deletion
            if (not self.leftchild) and (not self.rightchild):
                self._replace_with_child(None)
                return

            # Here, we know we have at least one child
            if not self.leftchild:  # must have only a rightchild
                self._replace_with_child(self.rightchild)
                return
            if not self.rightchild:  # must have only a leftchild
                self._replace_with_child(self.leftchild)
                return

            # Here, we must do the two-child deletion (same as in plain bst,
            # only copy the value)
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
            return self.rightchild.delete(val)

        # If we get here it'll be on the left
        if not self.leftchild:
            return
        return self.leftchild.delete(val)

    def _replace(self, newnode):
        """Replace self with newnode (possibly None, possibly with its
        own children)"""
        if not self.parent:
            if not newnode:
                self.value = None
                self._EMPTY = True
                self.leftchild = None
                self.rightchild = None
                self.color = BLACK
                return
            self.value = newnode.value
            self.leftchild = newnode.leftchild
            self.rightchild = newnode.rightchild
            self.color = newnode.color
            return

        if self.parent.leftchild and self.parent.leftchild is self:
            self.parent.leftchild = newnode
        else:  # We must be the right child
            self.parent.rightchild = newnode
        if newnode:
            newnode.parent = self.parent

    def _replace_with_child(self, child):
        # CASE 1: we are RED (everything is fine, just remove self)
        if self.color is RED:
            self._replace(child)
            return
        else:  # We are black
            # CASE 2: child is red, just paint it black
            if child and (child.color is RED):
                child.color = BLACK
                self._replace(child)
                return
            # Now, both self & child are black (child is always None first time thru)
            # CASE 3: We are root
            if not self.parent:
                self._replace(child)
                return
            # CASE 4: Sibling is red
            if self.sibling and (self.sibling.color is RED):
                self.sibling.color, self.parent.color = \
                    self.parent.color, self.sibling.color
                if self is self.parent.leftchild:
                    self.parent._rotate_right()
                    # Need to update self now
                    self = self.parent.leftchild
                else:
                    self.parent._rotate_left()
                    # Need to update self now
                    self = self.parent.rightchild
                # Don't return or replace, move on to cases 6 and higher.
            # CASE 5: self, sibling, parent, and sibling's children are all black
            if self.sibling and (self.sibling.color is BLACK) \
                    and (self.parent.color is BLACK) \
                    and ((not self.sibling.leftchild)
                         or (self.sibling.leftchild.color is BLACK)) \
                    and ((not self.sibling.rightchild)
                         or (self.sibling.rightchild.color is BLACK)):
                self.sibling.color = RED
                self._replace(child)
                self.parent._replace_with_child(self.parent)
                return
            # CASE 6: parent red; self, sibling & sibling's children black
            # In this case we swap parent & siblings colors
            if self.sibling and (self.sibling.color is BLACK) \
                    and (self.parent.color is RED) \
                    and ((not self.sibling.leftchild)
                         or (self.sibling.leftchild.color is BLACK)) \
                    and ((not self.sibling.rightchild)
                         or (self.sibling.rightchild.color is BLACK)):
                self.sibling.color, self.parent.color = \
                    self.parent.color, self.sibling.color
                self._replace(child)
                return
            # CASE 7: sibling black, sibling.leftchild is red, sibling.rightchild is black,
            # self is leftchild of parent
            # OR mirror image
            # we rotate leftchild up to sibling, make old sibling red,
            # and it's old leftchild (new parent) black
            if self.parent.leftchild and (self.parent.leftchild is self) and \
                    self.sibling and (self.sibling.color is BLACK) \
                    and self.sibling.leftchild and (self.sibling.leftchild.color is RED) and \
                    ((self.sibling.rightchild is None) or (self.sibling.rightchild.color is BLACK)):
                self.sibling.color, self.sibling.leftchild.color = \
                    self.sibling.leftchild.color, self.sibling.color
                self.sibling._rotate_left()
                # Do not replace or return, continue to case 8
            if self.parent.rightchild and (self.parent.rightchild is self) and \
                    self.sibling and (self.sibling.color is BLACK) \
                    and self.sibling.rightchild and (self.sibling.rightchild.color is RED) and \
                    ((self.sibling.leftchild is None) or (self.sibling.leftchild.color is BLACK)):
                self.sibling.color, self.sibling.rightchild.color = \
                    self.sibling.rightchild.color, self.sibling.color
                self.sibling._rotate_right()
                # Do not replace or return, continue to case 8
            # CASE 8:  sibling is black, sibling's right child is red, and
            # self is the left child of its parent, or mirror image
            # We rotate sibling up to parent and swap sibling & parent's colors,
            # Make sibling's right (farthest from self) child black
            if self.parent.leftchild and (self.parent.leftchild is self) and \
                    self.sibling and (self.sibling.color is BLACK) \
                    and self.sibling.rightchild and (self.sibling.rightchild.color is RED):
                self.sibling.color, self.parent.color = self.parent.color, self.sibling.color
                self.sibling.rightchild.color = BLACK
                self.parent._rotate_right()
                # I think self is OK here
                print self.parent.value
                self._replace(child)
                return
            if self.parent.rightchild and (self.parent.rightchild is self) and \
                    self.sibling and (self.sibling.color is BLACK) \
                    and self.sibling.leftchild and (self.sibling.leftchild.color is RED):
                self.sibling.color, self.parent.color = self.parent.color, self.sibling.color
                self.sibling.leftchild.color = RED
                self.parent._rotate_left()
                # I think self is OK here
                print self.parent.value
                self._replace(child)
                return

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" \
            % (
                "" if self._EMPTY
                else ("\t%s [style=filled, fillcolor=black, fontcolor=white];"
                      "\n%s\n" %
                      (self.value, "\n".join(self._get_dot())))
            )

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        import random
        if self.leftchild:
            yield ("\t{0} [style=filled, fillcolor={1}, fontcolor={2}];" +
                   "\n\t{3} -> {0};").format(
                self.leftchild.value,
                "red" if self.leftchild.color is RED
                else "black",
                "white" if self.leftchild.color is BLACK
                else "black",
                self.value)
            for i in self.leftchild._get_dot():
                yield i
        elif self.rightchild:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.rightchild:
            yield ("\t{0} [style=filled, fillcolor={1}, fontcolor={2}];" +
                   "\n\t{3} -> {0};").format(
                self.rightchild.value,
                "red" if self.rightchild.color is RED
                else "black",
                "white" if self.rightchild.color is BLACK
                else "black",
                self.value)
            for i in self.rightchild._get_dot():
                yield i
        elif self.leftchild:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)

if __name__ == '__main__':
    import random
    # Setup for visualization
    rbt = RedBlackTree()
    while rbt.size() < 50:
        rbt.insert(random.randint(0, 1e4))
    assert rbt.size() == 50
    rbt.update_dot()
    print "Balance = ", rbt.balance()
