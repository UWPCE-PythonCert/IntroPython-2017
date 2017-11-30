"""
Kathryn Egan
"""


class SparseArray:

    def __init__(self, array=[]):
        self._data = {}
        self._length = len(array)
        for i, num in enumerate(array):
            if num != 0:
                self._data[i] = num

    @property
    def length(self):
        return self._length

    @property
    def data(self):
        return self._data

    def get_index(self, index):
        """ Maps negative index to corresponding positive index. """
        return index + self._length if index < 0 else index

    def __getitem__(self, index):
        """ Returns the item at given index or the items in
        the range if index is a slice object. """
        try:
            index = self.get_index(index)
        # index is a slice or tuple not an int
        except TypeError:
            try:
                return self.get_slice(index)
            # index is a tuple not a slice
            except AttributeError:
                result = SparseArray()
                for s in index:
                    result.extend(self.get_slice(s))
                return result
        else:
            if index >= self._length:
                raise IndexError
            if index in self._data:
                return self._data[index]
            return 0

    def get_slice(self, slice):
        """ Returns items in slice as another SparseArray. """
        # get start and raise error if past end of array
        start = 0 if not slice.start else self.get_index(slice.start)
        if start > self._length:
            raise IndexError
        # stop should not extend beyond end of array
        stop = (
            self._length if slice.stop is None
            else min(self._length, self.get_index(slice.stop)))
        # step is 1 if it is undefined, reverse _data if it is < 0
        step = 1 if slice.step is None else slice.step
        reverse = True if step < 0 else False
        step = step * -1 if step < 0 else step
        result = SparseArray()
        for i in range(start, stop, step):
            i = self._length - i - 1 if reverse else i
            value = self._data[i] if i in self._data else 0
            result.append(value)
        return result

    def to_list(self):
        """ Returns this SparseArray as a list. """
        result = [
            self._data[index] if index in self._data else 0
            for index in range(self._length)]
        return result

    def __setitem__(self, index, value):
        """ Sets item at given index to given value.
        Raises IndexError if index is out of range. """
        index = self.get_index(index)
        if index >= self._length:
            raise IndexError
        self._data[index] = value

    def __delitem__(self, index):
        """ Deletes item at given index.
        Raises IndexError if index is out of range. """
        index = self.get_index(index)
        if index >= self._length:
            raise IndexError
        deleted = {}
        for k, v in self._data.items():
            if k < index:
                deleted[k] = v
            elif k > index:
                deleted[k - 1] = v
        self._data = deleted
        self._length -= 1

    def __reversed__(self):
        """ Returns a new SparseArray that is a
        reversed version of this SparseArray. """
        rev = SparseArray()
        for key, value in self._data.items():
            rev._data[self._length - key - 1] = value
        rev._length = self._length
        return rev

    def __iter__(self):
        """ Yields items in this SparseArray in order. """
        for key in range(self._length):
            if key not in self._data:
                yield 0
            else:
                yield self._data[key]

    def __contains__(self, value):
        """ Returns whether this SparseArray contains given value. """
        if value == 0 and self._length > len(self._data):
            return True
        for k, v in self._data.items():
            if v == value:
                return True

    def __add__(self, other):
        new = SparseArray(self)
        new.extend(other)
        return new

    def __mul__(self, value):
        new = SparseArray()
        for i in range(value):
            new.extend(self)
        return new

    def __rmul__(self, value):
        return self.__mul__(value)

    def __eq__(self, other):
        """ Returns whether this SparseArray is equivalent to
        another SparseArray or another iterable. """
        if len(other) != self._length:
            return False
        for key, value in enumerate(other):
            if value != 0 and (
                    key not in self._data or self._data[key] != value):
                return False
        return True

    def __len__(self):
        """ Returns the _length of this array. """
        return self._length

    def __str__(self):
        """ Returns this SparseArray as a string. """
        return str(self.to_list())

    def __repr__(self):
        """ Returns a representation of this SparseArray. """
        return self.__str__()

    def append(self, value):
        """ Appends the given value to the end of this SparseArray. """
        if value != 0:
            self._data[self._length] = value
        self._length += 1

    def extend(self, other):
        """ Extends this SparseArray with the given array. """
        for num in other:
            self.append(num)

    def reverse(self):
        """ Reverses the items in this SparseArray. """
        self._data = self.__reversed__()._data

    def index(self, value):
        """ Returns first index of given value. """
        for index in range(self._length):
            result = self._data[index] if index in self._data else 0
            if result == value:
                return index
        raise ValueError
