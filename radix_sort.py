from __future__ import unicode_literals


def _get_nth_digit_from_right(n, number):
    """Return nth digit from right of number.
    For example, for n=2 and number=7483, return 8"""
    return number % (10 ** n) // (10 ** (n - 1))


def radix_sort_int(intlist):
    """Sorts POSITIVE integers using radix sort."""
    keep_going = True  # Keep track of if we have reached the highest digit
    buckets = [[] for j in xrange(10)]
    i = 1
    while keep_going:
        keep_going = False
        for value in intlist:
            buckets[_get_nth_digit_from_right(i, value)].append(value)

            if value > (10 ** i):
                keep_going = True

        i += 1
        intlist[:] = []
        for bucket in buckets:
            intlist.extend(bucket)
            bucket[:] = []


def radix_sort_str(strlist):
    """Sort a list of strings (in place) using radix sort. Case is ignored"""
    offset = ord('a') - 1  # We want a placeholder space before 'a', chr(96)
    max_length = 0
    for word in strlist:
        max_length = max(max_length, len(word))

    # Add placeholders so all words are max length
    for i, word in enumerate(strlist[:]):
        strlist[i] = word + chr(96) * (max_length - len(word))

    buckets = [[] for j in xrange(ord('z') - offset)]
    for i in xrange(1, max_length + 1):
        for word in strlist:
            buckets[ord(word[-i].lower()) - offset].append(word)
        strlist[:] = []
        for bucket in buckets:
            strlist.extend(bucket)
            bucket[:] = []

    strlist[:] = [word.strip(chr(96)) for word in strlist]


if __name__ == '__main__':
    import timeit
    cases = {'ordered': 'testlist = range(%d)',
             'random': 'import random; ' +
             'testlist = [random.randint(0, 1e6) for i in xrange(%d)]',
             'reversed': 'testlist = range(%d, 0, -1)'}

    pattern = """
On average, filling & sorting an array of %d %s numbers takes %e s"""

    for case in cases:
        for i in xrange(6, 15):
            length = 2 ** i
            print pattern % (length, case, timeit.timeit(
                "radix_sort_int(testlist)",
                setup="from __main__ import radix_sort_int;" +
                (cases[case] % length),
                number=10) / 10.)
