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
    rbt._preliminary_insert(10)
    assert rbt.value == 10
    assert rbt.color == RED
    rbt._preliminary_insert(8)
    assert rbt.leftchild.value == 8
    assert rbt.leftchild.color == RED
    rbt._preliminary_insert(12)
    assert rbt.rightchild.value == 12
    assert rbt.rightchild.color == RED
