"""
code that tests the AVLTree class defined in avl_tree.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from avl_tree import AVLTree
import random


def test_rotations():
    """Tests my rotations, balance, and depth with a simple AVLtree"""
    # Initialization etc. should work fine, just inherits from well-tested BST
    bintree = AVLTree()
    assert bintree.depth() == 0
    with pytest.raises(ValueError):
        bintree._rotate_left()
    bintree.insert(5)
    assert bintree.depth() == 1
    with pytest.raises(ValueError):
        bintree._rotate_left()
    with pytest.raises(ValueError):
        bintree._rotate_right()
    bintree.insert(3)
    assert bintree.depth() == 2
    with pytest.raises(ValueError):
        bintree._rotate_right()  # 3 is on left
    bintree._rotate_left()  # 3 now head
    bintree._rotate_right()  # 5 is head again
    bintree.insert(7)
    bintree.insert(6)
    bintree.insert(2)
    bintree.insert(4)
    bintree.insert(1)
    bintree.insert(9)
    bintree.insert(10)  # All in order, no rotations done
    #      5
    #    /   \
    #   3     7
    #  /\    / \
    # 2  4  6   9
    # |         |
    # 1         10
    bintree._rotate_right()
    #      7
    #    /   \
    #   5     9
    #  | \     \
    #  3  6    10
    #  /\
    # 2  4
    # |
    # 1
    assert bintree.value == 7
    assert bintree.balance() == 2
    assert bintree.size() == 9
    assert bintree.depth() == 5
    assert bintree.rightchild.value == 9
    assert bintree.leftchild.value == 5
    assert bintree.leftchild.rightchild.value == 6

    bintree.leftchild._rotate_left()
    # Note that this breaks stuff at head; the update of depth/_level is part
    # of insert()/delete(), so 7 never gets releveled without the next line
    bintree._relevel()
    #      7
    #    /   \
    #   3     9
    #  | \     \
    #  2  5    10
    # /  / \
    # 1  4  6
    assert bintree.balance() == 1
    assert bintree.depth() == 4
    pivot_node = bintree.leftchild
    assert pivot_node.value == 3
    assert pivot_node.leftchild.value == 2
    assert pivot_node.rightchild.value == 5


def test_avl_insertion():
    """Tests that avl insertion maintains balance"""
    bintree = AVLTree()
    for i in xrange(100):
        bintree.insert(random.randint(0, 1e6))
    assert bintree.size() == 100
    assert abs(bintree.balance()) < 2
    assert bintree.depth() < 9  # 2 ** 7 is 128, it should fit


def test_avl_deletion():
    """Tests that avl deletion maintains balance"""
    bintree = AVLTree()
    bintree.insert(10)
    bintree.insert(5)
    bintree.insert(15)
    bintree.insert(2)
    bintree.insert(7)
    bintree.insert(12)
    bintree.insert(30)
    bintree.insert(1)
    bintree.insert(11)
    bintree.insert(13)
    bintree.insert(35)
    bintree.insert(14)
    #           10
    #        /      \
    #       5       15
    #      / \     /  \
    #     2   7  12    30
    #    /      / \     \
    #   1      11 13    35
    #              \
    #              14
    # All inserted in an order such that no rotations occurred
    assert bintree.depth() == 5
    assert bintree.balance() == -1
    assert bintree.size() == 12
    bintree.delete(15)
    #           10
    #        /      \
    #       5       14
    #      / \     /  \
    #     2   7  12    30
    #    /      / \     \
    #   1      11 13    35
    # This is standard deletion, still in balance.
    # check that balance/depth update correctly
    assert bintree.balance() == 0
    assert bintree.depth() == 4
    assert bintree.size() == 11
    assert bintree.rightchild.depth() == 3
    assert bintree.rightchild.leftchild.depth() == 2
    assert bintree.rightchild.leftchild.balance() == 0  # used to be -1

    bintree.delete(7)
    #           10
    #        /      \
    #       5       14
    #      /       /  \
    #     2      12    30
    #    /      / \     \
    #   1      11 13    35
    # Now 5 is out of balance, rotate left up
    #           10
    #        /      \
    #       2       14
    #      / \     /  \
    #     1   5  12    30
    #           / \     \
    #          11 13    35
    assert bintree.leftchild.value == 2
    assert bintree.balance() == -1
    assert bintree.depth() == 4
    assert bintree.leftchild.depth() == 2
    assert bintree.leftchild.rightchild.depth() == 1

    bintree.delete(10)
    #           11
    #        /      \
    #       2       14
    #      / \     /  \
    #     1   5  12    30
    #             \     \
    #             13    35
    # Just normal deletion
    bintree.delete(11)
    #           12
    #        /      \
    #       2       14
    #      / \     /  \
    #     1   5  13    30
    #                   \
    #                   35
    # Just normal deletion
    bintree.delete(12)
    #           13
    #        /      \
    #       2       14
    #      / \        \
    #     1   5       30
    #                   \
    #                   35
    # Now 14 is out of balance, rotate 30 up
    #           13
    #        /      \
    #       2       30
    #      / \     /  \
    #     1   5   14  35
    assert bintree.depth() == 3
    assert bintree.balance() == 0
    assert bintree.value == 13
    assert bintree.leftchild.value == 2
    assert bintree.rightchild.value == 30
    assert bintree.leftchild.depth() == 2
    assert bintree.rightchild.depth() == 2
