from __future__ import unicode_literals


class Bucket(object):
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

    def add(self, key, value):
        if not self.next:  # We're empty
            self.key = key
            self.value = value
            self.next = Bucket()
        elif self.key == key:
            self.value = value  # Update
        else:
            self.next.add(key, value)

    def retrieve(self, key):
        if self.key == key:
            return self.value
        return self.next.retrieve(key)


class HashTable(object):
    def __init__(self, size):
        self.size = size
        self._slots = [Bucket() for i in xrange(size)]

    def hash(self, key):
        """Rotating hash (sort of assumes 32 bit ints, I think)"""
        if not (isinstance(key, str) or isinstance(key, unicode)):
            raise TypeError("Key must be a string")

        big_index = 0
        for letter in key:
            big_index = (big_index << 5) ^ (big_index >> 27) ^ ord(letter)

        return big_index % self.size

    def set(self, key, value):
        index = self.hash(key)
        self._slots[index].add(key, value)

    def get(self, key):
        index = self.hash(key)
        try:
            return self._slots[index].retrieve(key)
        except AttributeError:
            # Raised when we try going down a bucket with no next
            raise KeyError(key)
