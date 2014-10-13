"""
code that tests the DoublyLinkedList class defined in doubly_linked_list.py

can be run with py.test
"""
from __future__ import unicode_literals

import pytest  # used for the exception testing

import doubly_linked_list as d
# from stack import Node


def test_create():
    """Should raise TypeError if initialized with data, return a doubly linked list otherwise"""
    with pytest.raises(TypeError):
        d.DoublyLinkedList("a")
    assert isinstance(d.DoublyLinkedList(), d.DoublyLinkedList)


def test__insert():
    """insert(val) will insert the value 'val' at the head of the list"""
    dll = d.DoublyLinkedList()
    with pytest.raises(TypeError):
        dll.insert()

    #returns nothing
    assert dll.insert("blaguboo") is None
    assert dll.top.content == "blaguboo"
    assert dll.bottom.content == "blaguboo"
    dll.insert("one thing")
    dll.insert("second thing")
    assert dll.top.content == "second thing"
    assert dll.bottom.content == "blaguboo"
    #push still works, too.


def test_append():
    """append(val) will append the value 'val' at the tail of the list"""
    dll = d.DoublyLinkedList()
    with pytest.raises(TypeError):
        dll.append()
    # returns nothing, we have no way of getting at stuff yet
    assert dll.append("blaguboo") is None
    assert dll.top.content == "blaguboo"
    assert dll.bottom.content == "blaguboo"
    dll.append("one thing")
    dll.append("second thing")
    assert dll.bottom.content == "second thing"
    assert dll.top.content == "blaguboo"


def test_pop():
    '''Should return top data & remove it, raise IndexError if empty'''
    dll = d.DoublyLinkedList()
    with pytest.raises(IndexError) as err:
        dll.pop()
        assert "empty" in err.value
    dll.insert(10)
    dll.insert(9)
    assert dll.pop() == 9
    assert dll.pop() == 10
    assert dll.top is None
    assert dll.bottom is None
    with pytest.raises(IndexError) as err:
        dll.pop()
        assert "empty" in err.value


def test_shift():
    """shift() will remove the last value from the tail of the list and return it."""
    dll = d.DoublyLinkedList()
    with pytest.raises(IndexError) as err:
        dll.shift()
        assert "empty" in err.value
    dll.insert(10)
    dll.insert(9)
    assert dll.shift() == 10
    assert dll.shift() == 9
    assert dll.top is None
    assert dll.bottom is None
    with pytest.raises(IndexError) as err:
        dll.pop()
        assert "empty" in err.value


def test_remove():
    """remove(val) should remove the first node with the given val from the list, wherever it might be
    if node is not an item in the list, raises IndexError"""
    dll = d.DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)

    with pytest.raises(TypeError):
        dll.remove()
        dll.remove("adfe", 5)
    with pytest.raises(IndexError):
        dll.remove(8)

    assert dll.remove(2) is None
    assert dll.search(2) is None
    assert dll.search(3).next.content == 1  # i.e., 3 goes to 1 now
    dll.remove(1)
    assert dll.top.content == 3
    assert dll.bottom.content == 3
    assert dll.top.next is None
    assert dll.top is dll.bottom
    assert dll.bottom.previous is None
    dll.remove(3)
    assert dll.top is None
    assert dll.bottom is None
