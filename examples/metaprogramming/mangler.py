#!/usr/bin/env python3


class NameMangler(type):  # deriving from type makes it a metaclass.

    def __new__(cls, clsname, bases, _dict):
        print("in new:", _dict.keys())
        uppercase_attr = {}
        for name, val in _dict.items():
            if not name.startswith('__'):
                if len(name) == 1:
                    uppercase_attr[name * 2] = val
                uppercase_attr[name] = val
            else:
                uppercase_attr[name] = val
        print("in new:", uppercase_attr.keys())
        return super().__new__(cls, clsname, bases, uppercase_attr)


class Foo(metaclass=NameMangler):
    x = 1
    y = 2
    fred = "this"


if __name__ == "__main__":
    f = Foo()
    print(f.x)
    print(f.X)
