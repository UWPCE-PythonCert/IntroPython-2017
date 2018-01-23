
def NameError():
    print(something_not_defined)

def TypeError():
    stringvalue="foo"
    print(stringvalue + 10)

def SyntaxError():
    i_am_a_syntax_error

def AttributeError():
    integervalue=1
    print(integervalue.upper())

#NameError()
#TypeError()
#SyntaxError()
AttributeError()

