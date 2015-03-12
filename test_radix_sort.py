"""
code that tests the radix_sort functions defined in radix_sort.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from radix_sort import radix_sort_int, radix_sort_str
from radix_sort import _get_nth_digit_from_right


def test_input():
    # Checks that it needs a list of ints or a list of strings
    with pytest.raises(TypeError):
        radix_sort_int()

    with pytest.raises(TypeError):
        radix_sort_str()

    d = {1: 'one', 2: 'two'}
    with pytest.raises(TypeError):
        radix_sort_str(d)

    with pytest.raises(TypeError):
        radix_sort_int(None)

    with pytest.raises(TypeError):
        radix_sort_str(None)

    with pytest.raises(TypeError):
        radix_sort_int("Hello")
    with pytest.raises(TypeError):
        radix_sort_int(["Hello", "GoodBye"])

    with pytest.raises(TypeError):
        radix_sort_str([1, 2, 3, 4])


def test_get_digit():
    for i in xrange(10):
        assert _get_nth_digit_from_right(1, 120 + i) == i
        assert _get_nth_digit_from_right(2, 103 + i * 10) == i
        assert _get_nth_digit_from_right(3, 1024 + i * 100) == i
        assert _get_nth_digit_from_right(4, 10427 + i * 1000) == i
        assert _get_nth_digit_from_right(4, 11) == 0


def test_sorting_ints():
    import random
    datalist = [random.randint(0, 1e6) for i in xrange(100)]
    print datalist
    radix_sort_int(datalist)
    print datalist
    previous = datalist[0]
    for i in datalist[1:]:
        assert previous <= i
        previous = i


def test_sorting_strs():
    stringlist = ["You", "probably", "havent", "heard", "of", "them", "master",
                  "cleanse", "DIY", "deep", "v", "vinyl", "Shoreditch",
                  "heirloom", "ethical", "roof", "party", "mixtape", "iPhone"]
    radix_sort_str(stringlist)
    assert stringlist == ['cleanse',
                          'deep',
                          'DIY',
                          'ethical',
                          'havent',
                          'heard',
                          'heirloom',
                          'iPhone',
                          'master',
                          'mixtape',
                          'of',
                          'party',
                          'probably',
                          'roof',
                          'Shoreditch',
                          'them',
                          'v',
                          'vinyl',
                          'You']
