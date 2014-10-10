#!/usr/bin/env python

"""
code that tests the circle class defined in circle.py

can be run with py.test
"""

import pytest  # used for the exception testing

import stack as s


def test_create():
    """Should raise TypeError if initialized with data, return a stack otherwise"""
    with pytest.raises(TypeError):
        s.Stack("a")
    assert isinstance(s.Stack(), s.Stack)


def test_push():
    """Should be able to push something to the stack, fail if nothing"""
    stack = s.Stack()
    with pytest.raises(TypeError):
        stack.push()

    #returns nothing
    assert stack.push("blaguboo") is None


def test_pop():
    '''Should return top data & remove it, raise IndexError if empty'''
    stack = s.Stack()
    with pytest.raises(IndexError) as err:
        stack.pop()
        assert "empty stack" in err.value
    stack.push(10)
    stack.push(9)
    assert stack.pop() == 9
    assert stack.pop() == 10
    with pytest.raises(IndexError) as err:
        stack.pop()
        assert "empty stack" in err.value
