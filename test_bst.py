"""
code that tests the BST (binary search tree) class defined in bst.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from bst import BST
import random


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
    assert not bintree.leftchild.rightchild  # 4 is gone
    assert bintree.delete(10) is None
    assert bintree.size() == 6
    assert not bintree.rightchild.rightchild.leftchild  # 9 is a leaf
    assert not bintree.rightchild.rightchild.rightchild
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
    assert bintree.leftchild.balance() == 1  # The subtree at 3 is left-heavy
    assert bintree.delete(3) is None  # So this will delete left-style
    #      5
    #    /   \
    #   2     7
    #  /\    / \
    # 1  4  6   9
    #           |
    #          10
    assert bintree.size() == 8
    assert bintree.leftchild.value == 2
    assert bintree.balance() == -1  # The whole tree is now right-heavy
    assert bintree.delete(5) is None  # So deleting the top will go right-style
    #      6
    #    /   \
    #   2     7
    #  /\      \
    # 1  4      9
    #           |
    #          10
    assert bintree.value == 6
    assert bintree.size() == 7
    assert bintree.rightchild.value == 7
    assert bintree.balance() == -1


def test_in_order_traversal():
    """Returns a generator of values in the tree using in-order traversal"""
    import types
    bintree = BST()
    with pytest.raises(TypeError):
        bintree.in_order(1)  # No args/kwargs
    with pytest.raises(TypeError):
        bintree.in_order(None)

    assert isinstance(bintree.in_order(), types.GeneratorType)

    testlist = []
    for i in xrange(30):
        testval = random.random()
        bintree.insert(testval)
        testlist.append(testval)

    assert bintree.size() == 30
    ordered_generator = bintree.in_order()
    testlist.sort()

    for number in ordered_generator:
        assert number == testlist.pop(0)


def test_pre_post_order_traversal():
    """Tests both pre and post-order traversal"""
    import types
    bintree = BST()

    with pytest.raises(TypeError):
        bintree.pre_order(1)  # No args/kwargs
    with pytest.raises(TypeError):
        bintree.pre_order(None)

    assert isinstance(bintree.pre_order(), types.GeneratorType)

    with pytest.raises(TypeError):
        bintree.post_order(1)  # No args/kwargs
    with pytest.raises(TypeError):
        bintree.post_order(None)

    assert isinstance(bintree.post_order(), types.GeneratorType)

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
    pre_gen = bintree.pre_order()
    post_gen = bintree.post_order()

    assert pre_gen.next() == 5
    assert pre_gen.next() == 3
    assert pre_gen.next() == 2
    assert pre_gen.next() == 1
    assert pre_gen.next() == 4
    assert pre_gen.next() == 7
    assert pre_gen.next() == 6
    assert pre_gen.next() == 9
    assert pre_gen.next() == 10

    assert post_gen.next() == 1
    assert post_gen.next() == 2
    assert post_gen.next() == 4
    assert post_gen.next() == 3
    assert post_gen.next() == 6
    assert post_gen.next() == 10
    assert post_gen.next() == 9
    assert post_gen.next() == 7
    assert post_gen.next() == 5

    with pytest.raises(StopIteration):
        pre_gen.next()

    with pytest.raises(StopIteration):
        post_gen.next()


def test_breadth_first_traversal():
    """Tests breadth-first traversal"""
    import types
    bintree = BST()

    with pytest.raises(TypeError):
        bintree.breadth_first(1)  # No args/kwargs
    with pytest.raises(TypeError):
        bintree.breadth_first(None)

    assert isinstance(bintree.breadth_first(), types.GeneratorType)

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
    gen = bintree.breadth_first()

    assert gen.next() == 5
    assert gen.next() == 3
    assert gen.next() == 7
    assert gen.next() == 2
    assert gen.next() == 4
    assert gen.next() == 6
    assert gen.next() == 9
    assert gen.next() == 1
    assert gen.next() == 10

    with pytest.raises(StopIteration):
        gen.next()


def test_rebalance():
    """Tests my rebalancing algorithm"""
    bintree = BST()

    for i in xrange(100):
        bintree.insert(random.randint(0, 1e6))
    assert bintree.size() == 100

    original_depth = bintree.depth()

    bintree.rebalance()
    assert abs(bintree.balance()) < 2
    assert original_depth > bintree.depth()

    bintree = BST()

    for i in xrange(100):
        bintree.insert(i)  # Horribly unbalanced
    assert bintree.size() == 100
    assert bintree.depth() == 100
    assert bintree.balance() == -99

    bintree.rebalance()
    assert abs(bintree.balance()) < 2
    assert bintree.depth() < 10  # Much better, anyway
