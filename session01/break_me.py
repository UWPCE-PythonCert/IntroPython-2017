# Description: In the break_me.py file write four simple Python functions:
# Each function, when called, should cause an exception to happen
# Each function should result in one of the four most common exceptions you’ll find.
# for review: NameError, TypeError, SyntaxError, AttributeError
# Comment: Execute this script in Python3.6
# Last modified: 10/07/2017 - davidkan@


class PracticeExceptions:

    def __init__(self):
        """
        Creates a constructor when the instance is initialized
        """
        self.python = 'python'
        self.java = 'java'
        self.c_sharp = 'c#'

    @staticmethod
    def SyntaxErrorExample():
        """
        Function will demo a SyntaxError exception
        :return: None
        """
        a = 1
        b = 'b'
        try:
            eval("1 + a")
            eval("1 === b")
        except SyntaxError as s:
            print("That won't work. Try again")
            print(s)

    def AttributeErrorExample(self):
        """
        Function will demo an AttributeError exception
        :return: None
        """
        try:
            print(self.python)
            print(self.java)
            print(self.c_sharp)
            print(self.sql)
        except AttributeError as a:
            print("This does not exist. Try again.")
            print(a)

    @staticmethod
    def TypeErrorExample():
        """
        Function will demo a TypeError exception
        :param self:
        :return: None
        """
        a = 1
        b = 'b'
        try:
            eval("1 + a")
            eval("1 + b")
        except TypeError as t:
            print("That won't work. Try again")
            print(t)

    @staticmethod
    def NameErrorExample():
        """
        Function will demo a NameError exception
        :return: None
        """
        # Declare a variable and assign it a string
        school = "University of Washington"

        try:
            if school:
                print(schools)
        except NameError as n:
            print("The varable does not exist. Try again")
            print(n)


if __name__ == "__main__":
    """
    Create an instance of the class and call all four functions
    """
    # Create an instance
    common_errors = PracticeExceptions()

    # Call the functions
    common_errors.NameErrorExample()
    common_errors.TypeErrorExample()
    common_errors.SyntaxErrorExample()
    common_errors.AttributeErrorExample()


