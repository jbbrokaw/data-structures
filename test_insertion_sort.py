"""
code that tests the insertion_sort function defined in insertion_sort.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from insertion_sort import insertion_sort


def test_input():
    # Checks that it needs a list
    with pytest.raises(TypeError):
        insertion_sort()

    d = {1: 'one', 2: 'two'}
    with pytest.raises(KeyError):
        insertion_sort(d)

    with pytest.raises(TypeError):
        insertion_sort(None)


def test_sorting():
    import random
    datalist = []
    for i in xrange(100):
        datalist.append(random.randint(0, 1e8))
    previous = datalist[0]
    for i in datalist[1:]:
        assert previous < i
        previous = 1
