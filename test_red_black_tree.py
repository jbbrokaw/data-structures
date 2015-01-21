"""
code that tests the AVLTree class defined in avl_tree.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from red_black_tree import RedBlackTree, RED, BLACK
# import random

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
    rbt.insert(12)
    assert rbt.rightchild.grandparent is None
    assert rbt.rightchild.rightchild.grandparent is rbt

def test_uncle():
    rbt = RedBlackTree()
    assert rbt.uncle is None
    rbt.insert(10)  # .    10
    rbt.insert(12)  # .   /  \
    rbt.insert(11)  # .  8   12
    rbt.insert(13)  # . / \  / \
    rbt.insert(8)  # . 7  9 11  13
    rbt.insert(7)
    rbt.insert(9)
    assert rbt.rightchild.uncle is None
    assert rbt.leftchild.uncle is None
    assert rbt.rightchild.rightchild.uncle.value == 8
    assert rbt.rightchild.leftchild.uncle.value == 8
    assert rbt.leftchild.rightchild.uncle.value == 12
    assert rbt.leftchild.leftchild.uncle.value == 12

def test_cases_one_through_three():
    rbt = RedBlackTree()
    # Case 1, root is head
    rbt.insert(10)
    assert rbt.color is BLACK
    # Case 2, current node's parent is black
    rbt.insert(12)
    assert rbt.color is BLACK
    assert rbt.rightchild.color is RED

    # Case 3A, parent is red, uncle doesn't exist
    rbt.insert(11)
    # 10(B)
    # . \
    # . 12(B)
    # . /
    # 11(R)
    child = rbt.rightchild.leftchild
    assert child.color is RED
    assert rbt.rightchild is child.parent
    assert child.parent.color is BLACK
    assert rbt.color is BLACK

    # Case 3B, parent and uncle are both RED
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
