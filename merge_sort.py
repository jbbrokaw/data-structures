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


def _shift_right(datalist, start, end):
    """Shifts elements datalist[start] to datalist[end - 1] into slots
    datalist[start + 1], datalist[end] without creating any copies.
    Overwrites datalist[end] (which must be allocated)."""
    index = end
    while index > start:
        datalist[index] = datalist[index - 1]
        index -= 1


def merge_in_place(datalist, start, end):
    """Merge the two sorted sublists from start to halfway (right) and from
    halfway to end - 1 (left) into one sorted list from start to end - 1"""
    halfway = (end - start) // 2 + start
    left_pointer = start
    right_pointer = halfway
    shifts = 0
    while left_pointer < (halfway + shifts):
        while (right_pointer < end) and \
                (datalist[right_pointer] < datalist[left_pointer]):
            tmp = datalist[right_pointer]
            _shift_right(datalist, left_pointer, right_pointer)
            datalist[left_pointer] = tmp
            left_pointer += 1
            right_pointer += 1
            shifts += 1
        left_pointer += 1


def merge_sort_in_place(datalist, start=0, end=None):
    """Merge sort in-place. Avoids making copies of the list but runs in
    non-linearithmic quasilinear time O(n log2 n) (because of the shifts).
    Runs much better on sorted lists (because no shifts needed)"""
    if end is None:
        end = len(datalist)
    size = end - start
    if size <= 1:
        return
    halfway = size // 2 + start
    merge_sort_in_place(datalist, start, halfway)
    merge_sort_in_place(datalist, halfway, end)
    merge_in_place(datalist, start, end)

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

    pattern = """
On average, filling & sorting an array of %d %s numbers in place takes %e s"""

    for case in cases:
        for i in xrange(6, 13):
            length = 2 ** i
            print pattern % (length, case, timeit.timeit(
                "merge_sort_in_place(testlist)",
                setup="from __main__ import merge_sort_in_place;" +
                (cases[case] % length),
                number=10) / 10.)
