"""
code that tests the circle class defined in circle.py

can be run with py.test
"""
from __future__ import unicode_literals

import pytest  # used for the exception testing

import linked_list as l
from stack import Node


def test_create():
    """Should raise TypeError if initialized with data, return a linked list otherwise"""
    with pytest.raises(TypeError):
        l.Linked_list("a")
    assert isinstance(l.Linked_list(), l.Linked_list)


def test_insert():
    """Should be able to insert something at the head of the list, fail if nothing"""
    llst = l.Linked_list()
    with pytest.raises(TypeError):
        llst.insert()

    #returns nothing
    assert llst.insert("blaguboo") is None

    #push still works, too.


def test_pop():
    '''Should return top data & remove it, raise IndexError if empty'''
    llst = l.Linked_list()
    with pytest.raises(IndexError) as err:
        llst.pop()
        assert "empty" in err.value
    llst.push(10)
    llst.push(9)
    assert llst.pop() == 9
    assert llst.pop() == 10
    with pytest.raises(IndexError) as err:
        llst.pop()
        assert "empty" in err.value


def test_size():
    """Should return the correct size"""
    llst = l.Linked_list()
    assert llst.size() == 0
    for i in xrange(5):
        llst.insert(i)
    assert llst.size() == 5
    llst.pop()
    assert llst.size() == 4


def test_search():
    """Should return the node containing 'val' in the list, if present, else None"""
    llst = l.Linked_list()
    with pytest.raises(TypeError):
        llst.search()
        llst.search("adfe", 5)
    assert llst.search("AEREKLJRE") is None

    llst.insert(5)

    assert llst.search(5) is llst.top

    llst.insert(4)
    llst.insert(3)

    assert llst.search(5) is llst.top.next.next
    evalnode = llst.search(4)
    assert isinstance(evalnode, Node)
    assert evalnode.content == 4
    assert isinstance(evalnode.next, Node)
    evalnode = llst.search(5)
    assert evalnode.content == 5
    assert evalnode.next is None
    llst.pop()
    assert llst.search(3) is None


def test_remove():
    """remove(node) should remove the given node from the list, wherever it might be
    if node is not an item in the list, raises IndexError"""
    llst = l.Linked_list()
    llst.insert(1)
    llst.insert(2)
    llst.insert(3)

    with pytest.raises(TypeError):
        llst.remove()
        llst.remove("adfe", 5)
    with pytest.raises(IndexError):
        llst.remove(Node(2))

    assert llst.remove(llst.search(2)) is None
    assert llst.search(2) is None
    assert llst.search(3).next.content == 1  # i.e., 3 goes to 1 now


def test_printll(capsys):  # Python gets REALLY MAD if I call this just print().
    """Should print the list represented as a Python tuple literal: "(12, 'sam', 37, 'tango')" """
    llst = l.Linked_list()
    llst.insert(12)
    llst.insert('sam')
    llst.insert(37)
    llst.insert('tango')

    llst.printll()
    out, err = capsys.readouterr()
    assert out == "(12, 'sam', 37, 'tango')"
