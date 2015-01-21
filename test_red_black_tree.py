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
    assert rbt._grandparent() is None
    rbt.insert(10)
    rbt.insert(11)
    rbt.insert(12)
    assert rbt.rightchild._grandparent() is None
    assert rbt.rightchild.rightchild._grandparent() is rbt

