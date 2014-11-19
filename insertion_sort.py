from __future__ import unicode_literals


def insertion_sort(datalist):
    """Sort list in place by insertion sort"""
    for i in xrange(1, len(datalist)):
        j = i
        while (j > 0) and (datalist[j - 1] > datalist[j]):
            datalist[j - 1], datalist[j] = datalist[j], datalist[j - 1]
            j -= 1


if __name__ == '__main__':
    import timeit
    cases = {'ordered': 'testlist = range(%d)',
             'random': 'import random; ' +
             'testlist = [random.randint(0, 1e6) for i in xrange(%d)]',
             'reversed': 'testlist = range(%d, 0, -1)'}

    pattern = """
On average, filling & sorting an array of %d %s numbers takes %e s"""

    for case in cases:
        for i in xrange(6, 12):
            length = 2 ** i
            print pattern % (length, case, timeit.timeit(
                "insertion_sort(testlist)",
                setup="from __main__ import insertion_sort;" +
                (cases[case] % length),
                number=10) / 10.)
