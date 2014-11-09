"""
code that tests the hash table class defined in hashtable.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from hashtable import HashTable
from hashtable import Bucket
import io


def test_bucket():
    """Should add stuff & give it back based on keys"""
    bucket = Bucket()
    bucket.add("key1", "value1")
    assert bucket.retrieve("key1") == "value1"
    bucket.add("key2", "value2")
    assert bucket.retrieve("key1") == "value1"
    assert bucket.retrieve("key2") == "value2"
    # Resets stuff, too
    bucket.add("key1", "value3")
    assert bucket.retrieve("key1") == "value3"


def test_initialization():
    """The hash table should be of fixed size.  The number of slots is
    determined when the table is initialized: foo = HashTable(1024)"""

    with pytest.raises(TypeError):
        table = HashTable()  # Size required

    with pytest.raises(TypeError):
        table = HashTable("Big")  # Should be an int

    table = HashTable(100)

    assert len(table._slots) == 100
    assert table.size == 100

    assert isinstance(table._slots[0], Bucket)


def test_hash():
    """Testing properties of the has function. Takes a long time"""
    # There are 235886 words in my dictionary.
    # 1.6 * the expected size is 377418, ideal for performance
    ideal_size = 377418
    table = HashTable(ideal_size)
    word = "init"

    with pytest.raises(TypeError) as err:
        table.hash(12345)
        assert err.value == "Key must be a string"

    frequencies = dict()

    for i in xrange(ideal_size):
        frequencies[i] = 0

    with io.open('/usr/share/dict/words') as words:
        while word != "":
            word = words.readline().strip()
            hashval = table.hash(word)
            assert 0 <= hashval < 377418
            frequencies[hashval] += 1

    emptyslots = 0
    max_bucket_size = 0

    for i in frequencies:
        if frequencies[i] == 0:
            emptyslots += 1
        elif frequencies[i] > max_bucket_size:
            max_bucket_size = frequencies[i]

    print emptyslots, max_bucket_size

    # Should be roughly as many empty slots as filled slots
    # So, say, from 40% (2/5) to 60% (3/5) are empty
    # This also tests our "ideal_size" choice
    assert emptyslots > (ideal_size // 3)
    assert emptyslots > (ideal_size // 3)

    # And the maximum bucket size shouldn't be too big
    assert max_bucket_size < 10


def test_set_get():
    """set(key, val) should store the given val using the given key,
    get(key) should return the value stored with the given key"""
    # There are 235886 words in my dictionary.
    # 1.6 * the expected size is 377418, ideal for performance
    ideal_size = 377418
    table = HashTable(ideal_size)
    word = "init"

    table.set("hound", "puppy")
    assert table.get("hound") == "puppy"

    with pytest.raises(TypeError) as err:
        table.set(12345, "oogabooga")
        assert err.value == "Key must be a string"

    with pytest.raises(TypeError):
        table.set("oogabooga")  # key & value both required

    with pytest.raises(TypeError):
        table.get()  # key required

    with pytest.raises(TypeError) as err:
        table.set(12345)
        assert err.value == "Key must be a string"

    with io.open('/usr/share/dict/words') as words:
        while word != "":
            word = words.readline().strip()
            table.set(word, word)  # fill the table, key == value

    # Now, we should get the same stuff back.
    with io.open('/usr/share/dict/words') as words:
        while word != "":
            word = words.readline().strip()
            assert table.get(word) == word

    with pytest.raises(KeyError):
        table.get("alkejralekjreqr")

    # Should also be able to reset stuff
    assert table.get("bacon") == "bacon"
    table.set("bacon", "delicious")
    assert table.get("bacon") == "delicious"
