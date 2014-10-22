"""
code that tests the BST (binary search tree) class defined in bst.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from bst import BST


def test_init():
    """implement a heap that can be either min or max
    the choice is possible at initialization time.
    It defaults to an empty heap but allows initialization
    with an iterable"""
    assert isinstance(BST(), BST)
    with pytest.raises(TypeError):
        BST([1, 2, 3, 4])  # May implement this later

    with pytest.raises(TypeError):
        BST(1, 2, 3, 4)  # Also could be implemented (limited use though)


def test_insert():
    """insert(self, val) will insert the value val into the BST.
    If val is already present, it will be ignored."""
    bintree = BST()
    with pytest.raises(TypeError):
        bintree.insert()
    with pytest.raises(TypeError):
        bintree.insert(1, 2)
    # Will accept any value including None; behavior is on the user

    bintree.insert(1)
    bintree.insert(None)
    bintree.insert({1: "one", 2: "two"})
    bintree.insert([1, 2, 3, 4])
    bintree.insert((1, 2))


def test_contains():
    """contains(val) should return True if val is in the BST, False if not."""
    bintree = BST()
    with pytest.raises(TypeError):
        bintree.insert()
    with pytest.raises(TypeError):
        bintree.insert(1, 2)
    # Will accept any value including None; behavior is on the user

    assert bintree.contains(None) is False
    assert bintree.contains(1) is False
    bintree.insert(1)
    assert bintree.contains(1) is True
    for i in xrange(-5, 5):
        bintree.insert(i)
    for i in xrange(-5, 5):
        assert bintree.contains(i) is True
    assert bintree.contains(None) is False


def test_size():
    """size(self) should return the integer size of the BST (total number of
    values stored in the tree), 0 if the tree is empty."""
    bintree = BST()
    with pytest.raises(TypeError):
        bintree.size(1)  # No values allowed

    assert bintree.size() == 0
    bintree.insert(5)
    assert bintree.size() == 1
    for i in xrange(10):
        bintree.insert(i)
    # 5 will be discarded (This is the first time we can really test this)
    assert bintree.size() == 10
    bintree.insert(10)
    assert bintree.size() == 11
    bintree.insert(-1)
    assert bintree.size() == 12


def test_depth():
    """depth(self) should return an integer representing the total number of
    levels in the tree. If there is one value, the depth should be 1, if two
    values it will be 2, if three values it may be 2 or three, depending."""
    bintree = BST()
    with pytest.raises(TypeError):
        bintree.depth(1)  # No values allowed

    assert bintree.depth() == 0
    bintree.insert(5)
    #   5
    assert bintree.depth() == 1
    bintree.insert(3)
    #   5
    #  /
    # 3
    assert bintree.depth() == 2
    bintree.insert(7)
    #   5
    #  / \
    # 3   7
    assert bintree.depth() == 2
    bintree.insert(2)
    bintree.insert(4)
    #     5
    #    / \
    #   3   7
    #  /\
    # 2  4
    assert bintree.depth() == 3
    bintree.insert(1)
    bintree.insert(6)
    #     5
    #    / \
    #   3   7
    #  /\   /
    # 2  4  6
    # |
    # 1
    assert bintree.depth() == 4
    ## and so on!


def test_balance():
    """balance(self) should return a positive or negative integer that
    represents how well balanced the tree is. Trees deeper on the left return a
    positive value, trees deeper on the right return a negative value.
    An ideally-balanced tree should return 0."""
    bintree = BST()
    with pytest.raises(TypeError):
        bintree.balance(1)  # No values allowed

    assert bintree.balance() == 0  # Empty tree
    bintree.insert(5)
    #   5
    assert bintree.balance() == 0  # no children, it's balanced
    bintree.insert(3)
    #   5
    #  /
    # 3
    assert bintree.balance() == 1  # Deeper on the left
    bintree.insert(7)
    #   5
    #  / \
    # 3   7
    assert bintree.balance() == 0
    bintree.insert(2)
    bintree.insert(4)
    #     5
    #    / \
    #   3   7
    #  /\
    # 2  4
    assert bintree.balance() == 1  # Deeper on the left
    bintree.insert(1)
    #     5
    #    / \
    #   3   7
    #  /\
    # 2  4
    # |
    # 1
    assert bintree.balance() == 2
    bintree.insert(9)
    bintree.insert(10)
    #     5
    #    / \
    #   3   7
    #  /\    \
    # 2  4    9
    # |       |
    # 1       10
    assert bintree.balance() == 0
    bintree.insert(12)
    assert bintree.balance() == -1
    # etc.!


def test_delete_no_children():
    """delete(self, val) should remove val from the tree if present,
    if not present it should do nothing. Return None in all cases"""
    bintree = BST()
    with pytest.raises(TypeError):
        bintree.delete()  # 1 value required

    bintree.insert(5)
    bintree.insert(3)
    bintree.insert(7)
    bintree.insert(2)
    bintree.insert(4)
    bintree.insert(1)
    bintree.insert(9)
    bintree.insert(10)
    #     5
    #    / \
    #   3   7
    #  /\    \
    # 2  4    9
    # |       |
    # 1       10
    assert bintree.size() == 8
    assert bintree.delete(-1) is None
    assert bintree.size() == 8
    assert bintree.delete(4) is None
    assert bintree.size() == 7
    assert not hasattr(bintree.leftchild, "rightchild")  # 4 is gone
    assert bintree.delete(10) is None
    assert bintree.size() == 6
    assert not hasattr(bintree.rightchild.rightchild, "leftchild")
    assert not hasattr(bintree.rightchild.rightchild, "rightchild")
    # 10 is gone


def test_delete_one_child():
    """delete(self, val) should remove val from the tree if present,
    if not present it should do nothing. Return None in all cases"""
    bintree = BST()
    bintree.insert(5)
    bintree.insert(3)
    bintree.insert(7)
    bintree.insert(2)
    bintree.insert(4)
    bintree.insert(1)
    bintree.insert(9)
    bintree.insert(10)
    #     5
    #    / \
    #   3   7
    #  /\    \
    # 2  4    9
    # |       |
    # 1       10
    assert bintree.size() == 8
    assert bintree.delete(7) is None
    #     5
    #    / \
    #   3   9
    #  /\    \
    # 2  4    10
    # |
    # 1
    assert bintree.size() == 7
    assert not bintree.contains(7)
    assert bintree.contains(9)
    assert bintree.contains(10)
    assert bintree.balance() == 1
    assert bintree.delete(2) is None
    #     5
    #    / \
    #   3   9
    #  /\    \
    # 1  4    10
    assert bintree.size() == 6
    assert not bintree.contains(2)
    assert bintree.contains(1)
    assert bintree.leftchild.leftchild.value == 1
    assert bintree.balance() == 0


def test_find_minimum_and_delete():
    """Should return the minimum value in a (sub)tree and delete that leaf"""
    bintree = BST()
    bintree.insert(5)
    bintree.insert(3)
    bintree.insert(7)
    bintree.insert(2)
    bintree.insert(4)
    bintree.insert(1)
    bintree.insert(9)
    bintree.insert(10)
    #     5
    #    / \
    #   3   7
    #  /\    \
    # 2  4    9
    # |       |
    # 1       10
    assert bintree.size() == 8
    assert bintree._find_minimum_and_delete() == 1
    #     5
    #    / \
    #   3   7
    #  /\    \
    # 2  4    9
    #         |
    #         10
    assert bintree.size() == 7
    bintree.rightchild._find_minimum_and_delete() == 7
    # The "head" of the right subtree is deleted in this case
    #     5
    #    / \
    #   3   9
    #  /\    \
    # 2  4    10
    assert bintree.size() == 6
    assert bintree.rightchild.value == 9


def test_delete_two_children():
    bintree = BST()
    bintree.insert(5)
    bintree.insert(3)
    bintree.insert(7)
    bintree.insert(6)
    bintree.insert(2)
    bintree.insert(4)
    bintree.insert(1)
    bintree.insert(9)
    bintree.insert(10)
    #      5
    #    /   \
    #   3     7
    #  /\    / \
    # 2  4  6   9
    # |         |
    # 1         10
    assert bintree.size() == 9
    assert bintree.delete(3) is None
    #     5
    #    / \
    #   4   7
    #  /   / \
    # 2   6   9
    # |       |
    # 1       10
    assert bintree.size() == 8
    assert bintree.leftchild.value == 4

    assert bintree.delete(5) is None
    #     6
    #    / \
    #   4   7
    #  /     \
    # 2       9
    # |       |
    # 1       10
    assert bintree.value == 6
    assert not hasattr(bintree.rightchild, "leftchild")
