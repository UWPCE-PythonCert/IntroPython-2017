"""
Kathryn Egan
"""


class SparseArray(list):
    """ Defines functionality for a sparse array. A sparse array
    stores only non-zero values.
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
        self._data = {}  # index : non-zero value
        self._length = len(array)  # length of array w/ zeros
        self._reversed = False  # array is reversed
        for i, num in enumerate(array):
            if num != 0:
                self._data[i] = num

    @property
    def data(self):
        """ Returns data as read-only variable, primarily for
        testing and debugging.
        Returns:
            dic int:int : indexes mapped to non-zero values
        """
        return self._data

    def _iforward(self, index):
        """ Converts a backwards index counting from end of array
        to a forward index starting counting from start of a array.
        Returns forward and None indexes as-is.
        E.g. for list length 5, -2 maps to 3, 2 maps to 2, None to None
        Args:
            index (int) : index to convert
        Returns:
            int :
                given index as forward index (counts from start of array)
                None if index is None
        """
        if index is not None:
            return len(self) + index if index < 0 else index

    def _ireverse(self, index):
        """ Reverses index to work with virtually reversed SparseArray.
        Returns None if index is None.
        Args:
            index (int) : index to reverse
        Returns:
            int : reversed index or None if index is None
        """
        if index is not None:
            return len(self) - index - 1

    def __getitem__(self, index):
        """ Returns the item at given index or the items in
        the range if index is a slice object. Raises IndexError
        if given index integer is outside scope of array. O(k * m)
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
            index = self._iforward(index)
        # index is a slice or tuple not an int O(k)
        except TypeError:
            try:
                return self._slice(index)
            # index is a tuple not a slice O(k * k) <-inefficient
            except AttributeError:
                result = SparseArray()
                for s in index:
                    result.extend(self._slice(s))
                return result
        else:  # O(1)
            if index < 0 or index >= len(self):
                raise IndexError('Index out of range')
            index = self._ireverse(index) if self._reversed else index
            if index in self._data:
                return self._data[index]
            return 0

    def _slice(self, slice):
        """ Returns items in slice as another SparseArray. O(k)
        Args:
            slice (slice) :
                slice object specifying start, stop, step of desired range
        Returns:
            SparseArray :
                SparseArray containing values in range specified by slice
        """
        from math import fabs
        step = 1 if slice.step is None else slice.step
        start = self._inormalize(slice.start, 0, step < 0)
        stop = self._inormalize(slice.stop, len(self), step < 0)
        result = SparseArray()
        for i in range(start, stop, int(fabs(step))):
            i = self._ireverse(i) if step < 0 else i
            result.append(self[i])
        return result

    def _inormalize(self, index, sub, reverse):
        """ Returns normalized index. Substitutes index with given
        sub if index is None, and reverses index if a reversed
        index is required. O(1)
        Args:
            index (int) : index to normalize
            initial (bool) : whether this index starts the desired array
            reverse (bool) : whether the desired array is reversed
        Returns:
            int : normalized index
        """
        # convert any backwards index to forwards
        index = self._iforward(index)
        # get reversed version of index if array is reversed
        index = self._ireverse(index) if reverse else index
        # apply limit if index does not exist
        index = sub if index is None else index
        # apply limit if index goes beyond either end of array
        index = self._ilimit(index)
        return index

    def _ilimit(self, index):
        """ Applies limit of 0 or length of array to index,
        whichever is closer to non-viable index. If this
        array has the given index, the index is returned as-is.
        E.g.:
            index of -7 for array of length 3 -> 0
            index of 2 for array of length 3 -> 2
            index of 7 for array of length 3 -> 3
        Args:
            index (int) : index to format
        Returns:
            int :
                0 for index preceding beginning of array
                length of array for index going past end of array
                otherwise, given index
        """
        index = max(0, index)
        index = min(len(self), index)
        return index

    def __setitem__(self, index, value):
        """ Sets item at given index to given value.
        Raises IndexError if index is out of range. O(1)
        Args:
            index (int) : index of value to change
            value (int) : desired value
        """
        index = self._iforward(index)
        if index < 0 or index >= len(self):
            raise IndexError('Index out of range')
        if value != 0:
            self._data[index] = value
        # setting a non-zero value to zero pops value
        elif index in self._data:
            self._data.pop(index)

    def __delitem__(self, index):
        """ Deletes item at given index.
        Raises IndexError if index is out of range. O(m)
        Args:
            index (int) : index of value to delete
        """
        index = self._iforward(index)
        if index < 0 or index >= len(self):
            raise IndexError('Index out of range')
        deleted = {}
        for k, v in self._data.items():
            if k < index:
                deleted[k] = v
            elif k > index:
                deleted[k - 1] = v
            # do not add deleted index to output
        self._data = deleted
        self._length -= 1

    def __iter__(self):
        """ Yields items in this SparseArray in order. O(n) """
        for key in range(len(self)):
            yield self[key]

    def __contains__(self, value):
        """ Returns whether this SparseArray contains given value. O(m)
        Args:
            value (int) : value to search for
        Returns:
            bool : whether given value is in SparseArray
        """
        # presence of zeros is determined by len of
        # stored data being less than virtual length
        if value == 0 and len(self) > len(self._data):
            return True
        for k, v in self._data.items():
            if v == value:
                return True

    def __add__(self, other):
        """ Adds given iterable to new SparseArray copy,
        returns copy. O(k)
        Args:
            other (iterable) : values to append to SparseArray
        Returns:
            SparseArray :
                new SparseArray copy with given values appended
        """
        new = SparseArray(self)
        new.extend(other)
        return new

    def __iadd__(self, other):
        """ Adds given iterable to this SparseArray and returns self.
        Args:
            other (iterable) : values to append SparseArray
        Returns:
            self : this SparseArray with values added
        """
        self.extend(other)
        return self

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
            if len(other) != len(self):
                return False
        # iterable with no length function
        except TypeError:
            pass
        for index, value in enumerate(other):
            if self[index] != value:
                return False
        return True

    def __ne__(self, other):
        """ Returns whether this SparseArray is not equivalent to
        another SparseArray or another iterable. O(k)
        Args:
            other (iterable) : object to compare
        Returns:
            bool :
                True if other is not equal this SparseArray, False otherwise
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """ Returns whether self is less than other object. O(k)
        Args:
            other (iterable) : object to compare
        Returns:
            bool :
                True if self is less than other
                False if self is greater than or equal to other
        """
        index = None
        for index, value in enumerate(other):
            # indexes in self exhausted = other is longer
            if len(self) <= index:
                return True
            if self[index] < value:
                return True
            if self[index] > value:
                return False
        return (
            False if index is None
            else index >= len(self))

    def __gt__(self, other):
        """ Returns whether self is greater than other object. O(k)
        Args:
            other (iterable) : object to compare
        Returns:
            bool :
                True if self is greater than other
                False if self is less than or equal to other
        """
        index = None
        for index, value in enumerate(other):
            # indexes in self exhausted = other is longer
            if len(self) <= index:
                return False
            if self[index] < value:
                return False
            if self[index] > value:
                return True
        return (
            0 < len(self) if index is None
            else index < len(self) - 1)

    def __le__(self, other):
        """ Returns whether self is less than or equal to other object. O(k)
        Args:
            other (iterable) : object to compare
        Returns:
            bool :
                True if self is less than or equal to other
                False if self is greater than other
        """
        return not self.__gt__(other)

    def __ge__(self, other):
        """ Returns whether self is greater than or equal to other object. O(k)
        Args:
            other (iterable) : object to compare
        Returns:
            bool :
                True if self is greater than or equal to other
                False if self is less than other
        """
        return not self.__lt__(other)

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
        return str(self)

    def append(self, value):
        """ Appends the given value to the end of this SparseArray. O(1)
        Args:
            value (int) : value to append to this SparseArray
        """
        if value != 0:
            self._data[len(self)] = value
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
        """ Provides an iterator on this SparseArray in reverse. O(m)? """
        for i in range(len(self)):
            yield self[self._ireverse(i)]

    def reverse(self):
        """ Reverses the items in this SparseArray by toggling
        variable indicating virtually reversed state. O(m) """
        self._reversed = not self._reversed

    def index(self, value):
        """ Returns first index of given value.
        Raises ValueError if value is not in this SparseArray. O(n)
        Args:
            value (int) : value to search for
        Returns:
            int : first index of value
        """
        for index in range(len(self)):
            if self[index] == value:
                return index
        raise ValueError('Value not in array')

    def insert(self, index, value):
        """ Inserts given value at given index. O(m)
        Args:
            index (int) : index to insert value at
            value (int) : value to insert
        """
        index = self._iforward(index)
        index = self._ilimit(index)
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
            return len(self) - len(self._data)
        return sum([1 for _, v in self._data.items() if v == value])
