"""
code that tests the Queue class defined in queue.py

can be run with py.test
"""
from __future__ import unicode_literals

import pytest  # used for the exception testing

import queue as q


def test_create():
    """Should raise TypeError if initialized with data, return a linked
    list otherwise"""
    with pytest.raises(TypeError):
        q.Queue("a")
    assert isinstance(q.Queue(), q.Queue)


def test_enqueue():
    """adds value to the queue"""
    queue = q.Queue()
    queue.enqueue(5)
    assert queue.back.content == 5
    assert queue.front.content == 5
    queue.enqueue(6)
    assert queue.back.content == 6
    assert queue.front.content == 5
    assert queue.back.previous.content == 5
    assert queue.back.next is None
    assert queue.front.next.content == 6
    assert queue.front.previous is None
    with pytest.raises(TypeError):
        queue.enqueue()
        queue.enqueue(1, 2)


def test_dequeue():
    """removes the correct item from the queue and returns its value
    (should raise an error if the queue is empty)"""
    queue = q.Queue()
    with pytest.raises(IndexError) as err:
        queue.dequeue()
        assert "empty queue" in err.value

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue([3])
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == [3]
    with pytest.raises(IndexError) as err:
        queue.dequeue()
        assert "empty queue" in err.value


def test_size():
    """returns the size of the queue.
    Should return 0 if the queue is empty."""
    queue = q.Queue()
    assert queue.size() == 0
    queue.enqueue((1, 2, 3, 4, 5))
    assert queue.size() == 1
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.size() == 4
    queue.dequeue()
    assert queue.size() == 3
    queue.dequeue()
    queue.dequeue()
    assert queue.size() == 1
    queue.dequeue()
    assert queue.size() == 0
