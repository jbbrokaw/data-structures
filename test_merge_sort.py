"""
code that tests the merge_sort function defined in merge_sort.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from merge_sort import merge_sort, merge
from merge_sort import merge_sort_in_place, merge_in_place, _shift_right


def test_input():
    # Checks that it needs a list
    with pytest.raises(TypeError):
        merge_sort()

    d = {1: 'one', 2: 'two'}
    with pytest.raises(TypeError):
        merge_sort(d)

    with pytest.raises(TypeError):
        merge_sort(None)


def test_merge():
    left = [1, 3, 5, 7]
    right = [2, 4, 5, 6, 8]
    assert merge(left, right) == [1, 2, 3, 4, 5, 5, 6, 7, 8]


def test_sorting():
    import random
    datalist = [random.randint(0, 1e6) for i in xrange(100)]
    datalist = merge_sort(datalist)

    previous = datalist[0]
    for i in datalist[1:]:
        assert previous <= i
        previous = i


def test_shift_right():
    testlist = [1, 2, 3, 4, 5, -1, 0]
    end = len(testlist)
    # Want to shift this right
    _shift_right(testlist, 0, end - 1)
    testlist[0] = 0
    assert len(testlist) == end
    assert testlist == [0, 1, 2, 3, 4, 5, -1]


def test_merge_in_place():
    testlist = [7, 12, 20, 4, 6, 22]
    merge_in_place(testlist, 0, len(testlist))
    assert testlist == [4, 6, 7, 12, 20, 22]
    testlist = [7, 12, 20, 4, 6, 18]
    merge_in_place(testlist, 0, len(testlist))
    assert testlist == [4, 6, 7, 12, 18, 20]


def test_merge_sort_in_place():
    import random
    datalist = [random.randint(0, 1e6) for i in xrange(100)]
    merge_sort_in_place(datalist)

    previous = datalist[0]
    for i in datalist[1:]:
        assert previous <= i
        previous = i
