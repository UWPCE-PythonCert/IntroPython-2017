#!/usr/bin/env python3
"""
Sparse array implementation
"""

class SparseArray(object):
    def __init__(self, number_array):
        self.__length = len(number_array)
        self.__array = {}

        for index, value in enumerate(number_array):
            if value != 0:
                self.__array[index] = value


    def construct_list(self):
        return [self.__array[i] if i in self.__array else 0 for i in
                range(self.__length)]


    def __str__(self):
        return "[{}]".format(",".join([str(i) for i in self.construct_list()]))


    def __repr__(self):
        return "[{}]".format(",".join([str(i) for i in self.construct_list()]))


    def __len__(self):
        return self.__length


    def __getitem__(self, index):
        if index > self.__length - 1:
            raise IndexError
        elif index not in self.__array:
            return 0
        return self.__array[index]


    def __delitem__(self, index):
        if index > self.__length - 1:
            raise IndexError
        else:
            for i in range(index, (self.__length - 1)):
                if (i+1) in self.__array:
                    self.__array[i] = self.__array[i+1]

            self.__array.pop((self.__length - 1), None)
            self.__length -= 1


    def __iter__(self):
        self.__index = 0
        return self


    def __next__(self):
        self.__index += 1

        if self.__length >= self.__index:
            if (self.__index - 1) in self.__array:
                return self.__array[(self.__index - 1)]
            return 0

        else:
            raise StopIteration


    def append(self, value):
        if value != 0:
            self.__array[self.__length] = value

        self.__length += 1
