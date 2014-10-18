"""
code that tests the Binheap class defined in binheap.py

can be run with py.test
"""
from __future__ import unicode_literals

import pytest  # used for the exception testing

import priorityq as p
import random


def test_init():
    """implement a heap that can be either min or max
    the choice is possible at initialization time.
    It defaults to an empty heap but allows initialization
    with an iterable"""
    assert isinstance(p.PriorityQueue(), p.PriorityQueue)
    assert isinstance(p.PriorityQueue([(i, "data") for i in xrange(10)]),
                      p.PriorityQueue)
    assert isinstance(p.PriorityQueue(prop="min"), p.PriorityQueue)


def test_insert():
    bin = p.PriorityQueue()
    bin.insert((0, "priority zero"))
    assert bin._data[0] == (0, "priority zero")
    bin.insert((1, "priority one"))
    assert bin._data[0] == (1, "priority one")
    assert bin._data[1] == (0, "priority zero")
    bin.insert((-1, "priority minus one"))
    assert bin._data[0] == (1, "priority one")
    assert bin._data[1] == (0, "priority zero")
    assert bin._data[2] == (-1, "priority minus one")

    bin = p.PriorityQueue(prop="min")
    bin.insert((0, "priority zero"))
    assert bin._data[0] == (0, "priority zero")
    bin.insert((1, "priority one"))
    assert bin._data[0] == (0, "priority zero")
    assert bin._data[1] == (1, "priority one")
    bin.insert((-1, "priority minus one"))
    assert bin._data[0] == (-1, "priority minus one")
    assert bin._data[1] == (1, "priority one")
    assert bin._data[2] == (0, "priority zero")
    with pytest.raises(ValueError) as err:
        bin.insert("Some stuff without a priority")
        assert "Only tuples" in err.value


def test_peek():
    bin = p.PriorityQueue()
    bin.insert((0, "zero"))        #        1
    assert bin.peek() == "zero"
    bin.insert((1, "one"))         #       / \
    assert bin.peek() == "one"
    bin.insert((-1, "minus one"))  #      0  -1

    assert bin.peek() == "one"
    assert bin._data[0] == (1, "one")
    assert bin._data[1] == (0, "zero")
    assert bin._data[2] == (-1, "minus one")


def test_pop():
    bin = p.PriorityQueue()
    for i in xrange(20):
        val = random.random()
        bin.insert((val, str(val)))

    for j in xrange(10):
        higher = bin.pop()
        lower = bin.pop()
        assert float(higher) > float(lower)

    with pytest.raises(IndexError):
        bin.pop()
