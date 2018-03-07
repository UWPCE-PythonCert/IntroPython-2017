
"""
Some example code for a decorator in side a class
"""


class TestDecorator:

    def _decorator(func):
        def inner(self, *args, **kwargs):
            print("decorated method is running")
            # doing something with self
            self.data = "something"
            return func(self, *args, **kwargs)
        return inner

    @_decorator
    def test(self, x, y):
        print("in test", x, y)

