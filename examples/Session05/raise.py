"""
raising exceptions
"""


def fun(x):
    if x < 0:
        raise ValueError("You must use a posative number")
    else:
        try:
            45 / x
        except ZeroDivisionError as err:
            print("doing something")
            print(err.args)
            err.args = (err.args[0] + "--A custom message",)
            err.random_info = "something"
            # print(dir(err))
            raise ValueError from err
        return "Success"




for a in [3, 6, -2, 4, 0, 34]:
    try:
        print(fun(a))
    except ValueError:
        pass

