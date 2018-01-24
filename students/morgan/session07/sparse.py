


class SparseArray:
    def __init__(self, number_array):
        self._length = len(number_array)
        self._array = {}

        for index, value in enumerate(number_array):
            if value != 0:
                self._array[index] = value

    def construct_list(self):
        return [self._array[i] if i in self._array else 0 for i in range(self._length)]

    def __str__(self):
        return "[{}]".format(",".join([str(i) for i in self.construct_list()]))

    def __repr__(self):
        return "[{}]".format(",".join([str(i) for i in self.construct_list()]))

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if index > self._length - 1:
            raise IndexError
        elif index not in self._array:
            return 0
        return self._array

    def __delitem__(self, index):
        if index > self._length -1:
            raise IndexError
        else:
            for i in range(index, (self._length - 1)):
                if (i+1) in self._array:
                    self._array[i] = self._array[i+1]
            self._array.pop((self._length -1), None)
            self._length -= 1

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        self._index += 1

        if self._length >= self._index:
            if (self._index - 1) in self._array:
                return self._array[(self._index -1)]
            return 0

        else:
            raise StopIteration

    def append(self, value):
        if value != 0:
            self._array[self._length] = value

        self._length += 1
