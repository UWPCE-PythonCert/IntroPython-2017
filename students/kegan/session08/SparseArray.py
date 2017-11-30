"""
Kathryn Egan
"""


class SparseArray:

    def __init__(self, array=[]):
        self.data = {}
        self.length = len(array)
        for i, num in enumerate(array):
            if num != 0:
                self.data[i] = num

    def __getitem__(self, key):
        key = key + self.length if key < 0 else key
        if key >= self.length:
            raise IndexError
        if key in self.data:
            return self.data[key]
        return 0

    def __setitem__(self, key, value):
        key = key + self.length if key < 0 else key
        if key >= self.length:
            raise IndexError
        self.data[key] = value

    def __delitem__(self, key):
        key = key + self.length if key < 0 else key
        if key >= self.length:
            raise IndexError
        deleted = {}
        for k, v in self.data.items():
            if k < key:
                deleted[k] = v
            elif k > key:
                deleted[k - 1] = v
        self.data = deleted
        self.length -= 1

    def __reversed__(self):
        rev = SparseArray()
        for key, value in self.data.items():
            rev.data[self.length - key - 1] = value
        rev.length = self.length
        return rev

    def __sorted__(self):
        s = SparseArray()
        # [sort protocol]
        return s

    def __iter__(self):
        for key in range(self.length):
            if key not in self.data:
                yield 0
            else:
                yield self.data[key]

    def __contains__(self, value):
        if value == 0 and self.length > len(self.data):
            return True
        for k, v in self.data.items():
            if v == value:
                return True

    def __eq__(self, other):
        if len(other) != self.length:
            return False
        for key, value in enumerate(other):
            if value != 0 and (
                    key not in self.data or self.data[key] != value):
                return False
        return True

    def __len__(self):
        return self.length

    def __str__(self):
        array = [
            self.data[key] if key in self.data else 0
            for key in range(self.length)]
        return str(array)

    def append(self, value):
        if value != 0:
            self.data[self.length] = value
        self.length += 1

    def extend(self, array):
        for num in array:
            self.append(num)

    def reverse(self):
        self.data = self.__reversed__().data
