from __future__ import unicode_literals


def insertion_sort(datalist):
    """Sort list in place by insertion sort"""
    for i in xrange(1, len(datalist)):
        j = i
        while (j > 0) and (datalist[j - 1] > datalist[j]):
            datalist[j - 1], datalist[j] = datalist[j], datalist[j - 1]
            j -= 1

if __name__ == '__main__':
    import random
    import timeit

    def fill_and_sort(n=100):
        datalist = []
        for i in xrange(n):
            datalist.append(random.randint(0, 1e8))
        insertion_sort(datalist)

    pattern = "On average, filling & sorting an array of %d numbers takes %e s"

    for i in xrange(6, 11):
        print pattern % (2 ** i, timeit.timeit(
            "fill_and_sort(%d)" % 2 ** i,
            setup="from __main__ import fill_and_sort",
            number=100) / 100.)
