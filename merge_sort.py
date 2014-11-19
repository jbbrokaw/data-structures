from __future__ import unicode_literals


def merge(sorted_left, sorted_right):
    """Merge two sorted lists"""
    merged_list = []
    index = 0
    for value in sorted_left:
        while (index < len(sorted_right)) and (sorted_right[index] < value):
            merged_list.append(sorted_right[index])
            index += 1
        merged_list.append(value)
    for value in sorted_right[index:]:
        merged_list.append(value)
    return merged_list


def merge_sort(datalist):
    """Sort datalist by merge sort"""
    size = len(datalist)
    if size <= 1:
        return datalist

    # We divide it up
    halfway = size // 2
    sorted_left = merge_sort(datalist[:halfway])
    sorted_right = merge_sort(datalist[halfway:])
    return merge(sorted_left, sorted_right)

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
                "merge_sort(testlist)",
                setup="from __main__ import merge_sort;" +
                (cases[case] % length),
                number=10) / 10.)
