"""
Kathryn Egan
"""


class SparseArray(list):
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
        self.data = {}  # index : non-zero value
        self.length = len(array)  # length of array w/ zeros
        self.rev = False  # array is reversed
        for i, num in enumerate(array):
            if num != 0:
                self.data[i] = num
    
    def positive_index(self, index):
        """ Maps a negative index to corresponding positive index.
        E.g. in list length 5, -2 maps to 3
        Args:
            index (int) : index to convert
        Returns:
            int : converted index
        """
        if index is not None:
            return len(self) + index if index < 0 else index

    def reverse_index(self, index):
        """ Reverses index to work with virtually reversed SparseArray.
        Args:
            index (int) : index to reverse
        Returns:
            int : reversed index
        """
        if index is not None:
            return len(self) - index - 1

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
            index = self.positive_index(index)
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
            if index < 0 or index >= len(self):
                raise IndexError
            index = self.reverse_index(index) if self.rev else index
            if index in self.data:
                return self.data[index]
            return 0

    def get_slice(self, slice):
        """ Returns items in slice as another SparseArray. O(k)
        Args:
            slice (slice) :
                slice object specifying start, stop, step of desired range
        Returns:
            SparseArray :
                SparseArray containing values in range specified by slice
        """
        from math import fabs
        if slice.step == 0:
            raise ValueError
        step = 1 if slice.step is None else slice.step
        start = self.get_index(slice.start, True, step < 0)
        stop = self.get_index(slice.stop, False, step < 0)
        result = SparseArray()
        for i in range(start, stop, int(fabs(step))):
            i = self.reverse_index(i) if step < 0 else i
            result.append(self[i])
        return result

    def get_index(self, index, initial, reverse):
        """ Returns normalized index according to whether it marks
        the beginning of the desired array and whether desired array
        is reversed.
        Args:
            index (int) : index to normalize
            initial (bool) : whether this index starts the desired array
            reverse (bool) : whether the desired array is reversed
        Returns:
            int : normalized index
        """
        limit = 0 if initial else len(self)
        # get positive version of index if it is negative
        index = self.positive_index(index)
        # get reversed version of index if array is reversed
        index = self.reverse_index(index) if reverse else index
        # apply limit if index does not exist
        index = limit if index is None else index
        # apply limit if index goes beyond either end of array
        index = max(limit, index) if initial else min(limit, index)
        return index

    def __setitem__(self, index, value):
        """ Sets item at given index to given value.
        Raises IndexError if index is out of range. O(1)
        Args:
            index (int) : index of value to change
            value (int) : desired value
        """
        index = self.positive_index(index)
        if index < 0 or index >= len(self):
            raise IndexError
        # setting a non-zero value to zero pops value from array
        if value != 0:
            self.data[index] = value
        elif index in self.data:
            self.data.pop(index)

    def __delitem__(self, index):
        """ Deletes item at given index.
        Raises IndexError if index is out of range. O(m)
        Args:
            index (int) : index of value to delete
        """
        index = self.positive_index(index)
        if index < 0 or index >= len(self):
            raise IndexError
        deleted = {}
        for k, v in self.data.items():
            if k < index:
                deleted[k] = v
            elif k > index:
                deleted[k - 1] = v
        self.data = deleted
        self.length -= 1

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
        if value == 0 and len(self) > len(self.data):
            return True
        for k, v in self.data.items():
            if v == value:
                return True

    def __add__(self, other):
        """ Adds given iterable to new SparseArray copy. O(k)
        Args:
            other (iterable) : values to append to SparseArray
        Returns:
            SparseArray : new SparseArray copy with given values appended
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
        for key, value in enumerate(other):
            if value != 0 and key not in self and self[key] != value:
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

    def __len__(self):
        """ Returns the length of this array including zeroes. O(1)
        Returns:
            int : length of SparseArray
        """
        return self.length

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
            self.data[len(self)] = value
        self.length += 1

    def extend(self, other):
        """ Extends this SparseArray with the given array. O(k)
        Args:
            other (iterable) :
                values to append to this SparseArray as iterable object
        """
        for num in other:
            self.append(num)

    def __reversed__(self):
        """ Provides an iterator on this SparseArray
        in reverse. O(m)
        """
        for i in range(len(self)):
            yield self[self.reverse_index(i)]

    def reverse(self):
        """ Reverses the items in this SparseArray. O(m) """
        self.rev = not self.rev

    def index(self, value):
        """ Returns first index of given value.
        Raises ValueError if value is not in this SparseArray. O(n)
        Args:
            value (int) : value to search for
        Returns:
            int : first index of value
        """
        for index in range(len(self)):
            result = self.data[index] if index in self.data else 0
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
        index = len(self) if index > len(self) else index
        # ensure any negative index is converted to positive
        index = (
            index if index >= 0
            else self.positive_index(max(len(self) * -1, index)))
        inserted = {}
        if value != 0:
            inserted[index] = value
        for i, v in self.data.items():
            i = i if i < index else i + 1
            inserted[i] = v
        self.data = inserted
        self.length += 1

    def count(self, value):
        """ Counts number of instances of value. O(m)
        Args:
            value (int) : value to count
        Returns:
            int : count of given value
        """
        if value == 0:
            return len(self) - len(self.data)
        return sum([1 for _, v in self.data.items() if v == value])
