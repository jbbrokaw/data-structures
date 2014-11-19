from __future__ import unicode_literals
from insertion_sort import insertion_sort


def quick_sort(datalist, start=0, end=None):
    if end is None:
        end = len(datalist)
    size = end - start
    if size <= 1:
        return

    halfway = size // 2 + start
    pivot_choices = [datalist[start], datalist[halfway], datalist[end - 1]]
    insertion_sort(pivot_choices)
    pivot = pivot_choices[1]
    left_pointer = start
    right_pointer = end - 1

    while left_pointer <= right_pointer:
        while datalist[left_pointer] < pivot:
            left_pointer += 1
        while datalist[right_pointer] > pivot:
            right_pointer -= 1
        if left_pointer <= right_pointer:
            datalist[left_pointer], datalist[right_pointer] = \
                datalist[right_pointer], datalist[left_pointer]
            left_pointer += 1
            right_pointer -= 1

    quick_sort(datalist, start, right_pointer + 1)
    quick_sort(datalist, left_pointer, end)


if __name__ == '__main__':
    import timeit
    cases = {'ordered': 'testlist = range(%d)',
             'random': 'import random; ' +
             'testlist = [random.randint(0, 1e6) for i in xrange(%d)]',
             'reversed': 'testlist = range(%d, 0, -1)'}

    pattern = """
On average, filling & sorting an array of %d %s numbers takes %e s"""

    for case in cases:
        for i in xrange(6, 13):
            length = 2 ** i
            print pattern % (length, case, timeit.timeit(
                "quick_sort(testlist)",
                setup="from __main__ import quick_sort;" +
                (cases[case] % length),
                number=10) / 10.)
