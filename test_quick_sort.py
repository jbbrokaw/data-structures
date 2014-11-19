"""
code that tests the quick_sort function defined in quick_sort.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from quick_sort import quick_sort


def test_input():
    # Checks that it needs a list
    with pytest.raises(TypeError):
        quick_sort()

    d = {1: 'one', 2: 'two'}
    with pytest.raises(KeyError):
        quick_sort(d)

    with pytest.raises(TypeError):
        quick_sort(None)


def test_sorting():
    import random
    datalist = [random.randint(0, 1e6) for i in xrange(100)]
    quick_sort(datalist)

    previous = datalist[0]
    for i in datalist[1:]:
        assert previous <= i
        previous = i
