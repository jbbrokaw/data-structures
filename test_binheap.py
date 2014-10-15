"""
code that tests the Binheap class defined in binheap.py

can be run with py.test
"""
from __future__ import unicode_literals

# import pytest  # used for the exception testing

import binheap as b


def test_init():
    """implement a heap that can be either min or max
    the choice is possible at initialization time.
    It defaults to an empty heap but allows initialization
    with an iterable"""
    assert isinstance(b.Binheap(), b.Binheap)
    assert isinstance(b.Binheap(xrange(10)), b.Binheap)
    assert isinstance(b.Binheap(prop="min"), b.Binheap)


def test_push():
    bin = b.Binheap()
    bin.push(0)
    assert bin._data[0] == 0
    bin.push(1)
    assert bin._data[0] == 1
    assert bin._data[1] == 0
    bin.push(-1)
    assert bin._data[0] == 1
    assert bin._data[1] == 0
    assert bin._data[2] == -1

    bin = b.Binheap(prop="min")
    bin.push(0)
    assert bin._data[0] == 0
    bin.push(1)
    assert bin._data[0] == 0
    assert bin._data[1] == 1
    bin.push(-1)
    assert bin._data[0] == -1
    assert bin._data[1] == 1
    assert bin._data[2] == 0
