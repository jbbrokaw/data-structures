"""
code that tests the merge_sort function defined in merge_sort.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from merge_sort import merge_sort, merge


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
