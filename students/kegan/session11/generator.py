

class intsum(object):

    def __init__(self):
        self._index = 0
        self._curr = 0

    def __next__(self):
        self._curr += self._index
        self._index += 1
        return self._curr

    def __iter__(self):
        return self


class doubler(object):

    def __init__(self):
        self.value = 1

    def __next__(self):
        temp = self.value
        self.value *= 2
        return temp

    def __iter__(self):
        return self


class fib(object):

    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __next__(self):
        temp = self.curr
        self.curr += self.prev
        self.prev = temp
        return self.prev

    def __iter__(self):
        return self


class prime(object):

    def __init__(self):
        self.curr = 1

    def __next__(self):
        self.curr += 1
        while True:
            temp = 2
            prime = True
            while temp <= self.curr / 2:
                if self.curr % temp == 0:
                    prime = False
                    break
                temp += 1
            if prime:
                return self.curr
            self.curr += 1

    def __iter__(self):
        return self
