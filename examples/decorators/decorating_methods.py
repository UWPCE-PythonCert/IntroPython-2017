



class Test:
    def __init__(self):
        self.messages = []

    def _test_dec(fun):
        def inner(self, *args, **kwargs):
            print("args are:", args)
            print("running the decorated version")
            self.messages.append(
                "{} was called with: args={}, kwargs={}".format(fun.__name__, args, kwargs))
            return fun(self, *args, **kwargs)
        return inner

    @_test_dec
    def test(self, a, b=5):
        print("test method running")
        print("a, b:", a, b)

    @_test_dec
    def test2(self, c, d=5):
        print("test2 method running")
        print("c, d:", c, d)
        return c + d


