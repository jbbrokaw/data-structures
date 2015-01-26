"""
code that tests the AVLTree class defined in avl_tree.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from red_black_tree import RedBlackTree, RED, BLACK
import random


def traverse_nodes(rbt, blacks=0):
    if rbt.color is BLACK:
        blacks += 1
    rbt.blacks = blacks

    if rbt.leftchild:
        for i in traverse_nodes(rbt.leftchild, rbt.blacks):
            yield i

    if not rbt._EMPTY:
        yield rbt

    if rbt.rightchild:
        for i in traverse_nodes(rbt.rightchild, rbt.blacks):
            yield i


def check_validity(rbt):
    """Ensure that the red-black tree exhibits all required properties"""
    assert rbt.parent is None  # Problems if we're not the head
    assert rbt.color is BLACK

    blacks = 0
    for j in traverse_nodes(rbt):
        # Test that all red nodes have black children (or None)
        if j.color is RED:
            if j.leftchild:
                assert j.leftchild.color is BLACK
            if j.rightchild:
                assert j.rightchild.color is BLACK

        # Test that all leaves (Nones) have the same number of blacks
        # in their paths
        blacks = max([blacks, j.blacks])
        if (j.leftchild is None) or (j.rightchild is None):
            assert j.blacks == blacks


def test_preliminary_insert():
    rbt = RedBlackTree()
    assert rbt.color == BLACK
    rbt.insert(10)
    assert rbt.value == 10
    assert rbt.color == BLACK  # Head stays black
    rbt.insert(8)
    assert rbt.leftchild.value == 8
    assert rbt.leftchild.color == RED
    rbt.insert(12)
    assert rbt.rightchild.value == 12
    assert rbt.rightchild.color == RED


def test_grandparent():
    rbt = RedBlackTree()
    assert rbt.parent is None
    assert rbt.grandparent is None
    rbt.insert(10)
    rbt.insert(11)
    rbt.insert(9)
    rbt.insert(12)
    assert rbt.rightchild.grandparent is None
    assert rbt.rightchild.rightchild.grandparent is rbt

def test_uncle():
    rbt = RedBlackTree()
    assert rbt.uncle is None
    rbt.insert(10)  # .    10
    rbt.insert(12)  # .   /  \
    rbt.insert(8)  # .   8   12
    rbt.insert(13)  # . / \  / \
    rbt.insert(7)  # . 7  9 11  13
    rbt.insert(11)
    rbt.insert(9)
    assert rbt.rightchild.uncle is None
    assert rbt.leftchild.uncle is None
    assert rbt.rightchild.rightchild.uncle.value == 8
    assert rbt.rightchild.leftchild.uncle.value == 8
    assert rbt.leftchild.rightchild.uncle.value == 12
    assert rbt.leftchild.leftchild.uncle.value == 12


def test_sibling():
    rbt = RedBlackTree()
    rbt.insert(10)  # .    10
    rbt.insert(12)  # .   /  \
    rbt.insert(8)  # .   8   12
    rbt.insert(13)  # . /    / \
    rbt.insert(7)  # . 7    11  13
    rbt.insert(11)
    assert rbt.sibling is None
    assert rbt.leftchild.sibling.value == 12
    assert rbt.rightchild.sibling.value == 8
    assert rbt.leftchild.leftchild.sibling is None
    assert rbt.rightchild.rightchild.sibling.value == 11


def test_cases_one_through_three():
    rbt = RedBlackTree()
    # Case 1, root is head
    rbt.insert(10)
    assert rbt.color is BLACK
    # Case 2, current node's parent is black
    rbt.insert(12)
    assert rbt.color is BLACK
    assert rbt.rightchild.color is RED

    # Case 3, parent and uncle are both RED
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(8)
    rbt.insert(12)
    rbt.insert(11)
    # .    10(B)
    # .   /  \
    # . 8(B) 12(B)
    # .      /
    # .   11(R)
    child = rbt.rightchild.leftchild
    assert child.color is RED
    assert rbt.rightchild is child.parent
    assert child.parent.color is BLACK
    assert child.uncle is rbt.leftchild
    assert child.uncle.color is BLACK
    assert rbt.color is BLACK


def test_cases_four_and_five():
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(12)
    rbt.insert(11)
    # Origin      Rotate for case 4   Rotate again Case 5
    # 10(B)     |    10(B)          |      11(B)
    # . \       |       \           |     /   \
    # . 12(R)   |       11(R)       |   10(R) 12(R)
    # . /       |         \         |
    # 11(R)     |         12(R)     |
    assert rbt.color is BLACK
    assert rbt.value == 11
    assert rbt.leftchild.color is RED
    assert rbt.leftchild.value == 10
    assert rbt.rightchild.color is RED
    assert rbt.rightchild.value == 12

def test_insertion():
    rbt = RedBlackTree()
    for i in xrange(256):
        rbt.insert(random.randint(0, 1e6))
    assert rbt.size() == 256
    assert abs(rbt.balance()) <= 1
    assert rbt.depth() <= 10

    check_validity(rbt)


# Need to demonstrate individual deletion cases, but show it works in general:
# def test_deletion():
#     numberpool = [random.randint(0, 1e4) for i in xrange(256)]
#     rbt = RedBlackTree()
#     for i in numberpool:
#         rbt.insert(i)
#         check_validity(rbt)
#     random.shuffle(numberpool)
#     for i in numberpool:
#         rbt.delete(i)
#         check_validity(rbt)
