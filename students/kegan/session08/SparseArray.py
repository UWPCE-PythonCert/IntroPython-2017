"""
Kathryn Egan
"""


class SparseArray:
    """ Defines functionality for a sparse array
    that stores only non-zero values.
    For all O notation,
      k = number of elements in parameter
      m = number of non-zero values in SparseArray
      n = number of values including virtual zeros in SparseArray
    """

    def __init__(self, array=[]):
        """ Initializes SparseArray. O(n)
        Args:
            array (iterable) :
                values to convert to SparseArray in an iterable object
        """
        self._data = {}
        self._length = len(array)
        self.is_reversed = False
        for i, num in enumerate(array):
            if num != 0:
                self._data[i] = num

    def _positive(self, index):
        """ Maps negative index to corresponding positive index.
        E.g. in list length 5, -2 maps to 3
        Args:
            index (int) : index to convert
        Returns:
            int : converted index
        """
        if index is not None:
            return len(self) + index if index < 0 else index

    def _reverse(self, index):
        if index is not None:
            return len(self) - index - 1 if self.is_reversed else index

    def __getitem__(self, index):
        """ Returns the item at given index or the items in
        the range if index is a slice object. O(k * m)
        Args:
            index (int or slice or tuple) :
                index of value to return
                slice object specifying indexes of values to return
                tuple of slice objects
        Returns:
            int or SparseArray :
                value at given index as integer or
                SparseArray containing values in range specified by slice(s)
        """
        try:
            index = self._positive(index)
        # index is a slice or tuple not an int O(k)
        except TypeError:
            try:
                return self.get_slice(index)
            # index is a tuple not a slice O(k * k) <-inefficient
            except AttributeError:
                result = SparseArray()
                for s in index:
                    result.extend(self.get_slice(s))
                return result
        else:  # O(1)
            if index >= self._length:
                raise IndexError
            if index in self._data:
                return self._data[index]
            return 0

    def get_slice(self, slice):
        """ Returns items in slice as another SparseArray. O(k)
        Args:
            slice (slice) :
                slice object specifying start, stop, and step of desired range
        Returns:
            SparseArray :
                SparseArray containing values in range specified by slice
        """
        if slice.step == 0:
            raise ValueError
        step = 1 if slice.step is None else slice.step
        self.is_reversed = True if step < 0 else False
        step = step * -1 if self.is_reversed else step
        start = self._positive(slice.start)
        stop = self._positive(slice.stop)
        start = self._reverse(start)
        stop = self._reverse(stop)
        start = 0 if start is None else start
        stop = len(self) if stop is None else stop
        start = max(0, start)
        stop = min(len(self), stop)
        input_data = reversed(self) if self.is_reversed else self
        result = SparseArray()
        for i in range(start, stop, step):
            value = input_data[i] if i in input_data else 0
            result.append(value)
        return result

    def __setitem__(self, index, value):
        """ Sets item at given index to given value.
        Raises IndexError if index is out of range. O(1)
        Args:
            index (int) : index of value to change
            value (int) : desired value
        """
        index = self._positive(index)
        if index >= self._length:
            raise IndexError
        self._data[index] = value

    def __delitem__(self, index):
        """ Deletes item at given index.
        Raises IndexError if index is out of range. O(n)
        Args:
            index (int) : index of value to delete
        """
        index = self._positive(index)
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

    def __iter__(self):
        """ Yields items in this SparseArray in order. O(n) """
        for key in range(self._length):
            if key in self._data:
                yield self._data[key]
            else:
                yield 0

    def __contains__(self, value):
        """ Returns whether this SparseArray contains given value. O(m)
        Args:
            value (int) : value to search for
        Returns:
            bool : whether given value is in SparseArray
        """
        if value == 0 and self._length > len(self._data):
            return True
        for k, v in self._data.items():
            if v == value:
                return True

    def __add__(self, other):
        """ Adds given iterable to this SparseArray. O(k)
        Args:
            other (iterable) : values to append to SparseArray
        Returns:
            SparseArray : this SparseArray with given values appended
        """
        new = SparseArray(self)
        new.extend(other)
        return new

    def __mul__(self, value):
        """ Multiplies this SparseArray by the given integer. O(k * m)
        Args:
            value (int) : number of copies of SparseArray in result
        Returns:
            SparseArray :
                new SparseArray with [value] number of copies of original
        """
        new = SparseArray()
        for i in range(value):
            new.extend(self)
        return new

    def __rmul__(self, value):
        """ Provides commutative multiplication for SparseArray. """
        return self.__mul__(value)

    def __eq__(self, other):
        """ Returns whether this SparseArray is equivalent to
        another SparseArray or another iterable. O(k)
        Args:
            other (iterable) : object to compare
        Returns:
            bool :
                True if other has same values and no more or fewer
                values that this SparseArray, False otherwise
        """
        try:
            if len(other) != self._length:
                return False
        except TypeError:
            pass
        for key, value in enumerate(other):
            if value != 0 and (
                    key not in self._data or self._data[key] != value):
                return False
        return True

    def __len__(self):
        """ Returns the length of this array including zeroes. O(1)
        Returns:
            int : length of SparseArray
        """
        return self._length

    def __str__(self):
        """ Returns this SparseArray as a string. O(n)
        Returns:
            str : this SparseArray as a string
        """
        return str(list(self))

    def __repr__(self):
        """ Returns a representation of this SparseArray. O(n)
        Returns:
            str : this SparseArray as a string
        """
        return self.__str__()

    def append(self, value):
        """ Appends the given value to the end of this SparseArray. O(1)
        Args:
            value (int) : value to append to this SparseArray
        """
        if value != 0:
            self._data[self._length] = value
        self._length += 1

    def extend(self, other):
        """ Extends this SparseArray with the given array. O(k)
        Args:
            other (iterable) :
                values to append to this SparseArray as iterable object
        """
        for num in other:
            self.append(num)

    def __reversed__(self):
        """ Returns a new SparseArray that is a
        reversed version of this SparseArray. O(m)
        Returns:
            SparseArray : reversed version of this SparseArray
        """
        rev = SparseArray()
        for key, value in self._data.items():
            rev._data[self._length - key - 1] = value
        rev._length = self._length
        return rev

    def reverse(self):
        """ Reverses the items in this SparseArray. O(m) """
        self._data = self.__reversed__()._data

    def index(self, value):
        """ Returns first index of given value.
        Raises ValueError if value is not in this SparseArray. O(n)
        Args:
            value (int) : value to search for
        Returns:
            int : first index of value
        """
        for index in range(self._length):
            result = self._data[index] if index in self._data else 0
            if result == value:
                return index
        raise ValueError

    def insert(self, index, value):
        """ Inserts given value at given index. O(m)
        Args:
            index (int) : index to insert value at
            value (int) : value to insert
        """
        # indexes > length of array will be considered end of array
        index = self._length if index > self._length else index
        # ensure any negative index is converted to positive
        index = (
            index if index >= 0
            else self._positive(max(self._length * -1, index)))
        inserted = {}
        if value != 0:
            inserted[index] = value
        for i, v in self._data.items():
            i = i if i < index else i + 1
            inserted[i] = v
        self._data = inserted
        self._length += 1

    def count(self, value):
        """ Counts number of instances of value. O(m)
        Args:
            value (int) : value to count
        Returns:
            int : count of given value
        """
        if value == 0:
            return self._length - len(self._data)
        return sum([1 for _, v in self._data.items() if v == value])
