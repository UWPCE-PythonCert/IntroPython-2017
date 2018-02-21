def function_builder(n):
    """function that returns a list of functions that increment the input"""
    funclist = []
    for i in range(n):
        funclist.append(lambda x, j=i: x + j)
    return funclist

def function_builder2(n):
    """same as above using a list comprehension"""
    return [lambda x, j=i: x + j for i in range(n)]
