def FizzBuzz(n):
    """print the first n numbers, if n is a multiple of 3 it will print Fizz,
        if n is a multiple of 5 it will print buzz, and if it is a multiple of both it
        will print FizzBuzz"""
    for i in range(1, n + 1):
        word = ""
        if (i) % 3 == 0:
            word += "Fizz"
        if (i) % 5 == 0:
            word += "Buzz"
        if len(word) > 0:
            print(word)
        else:
            print(i)


FizzBuzz(100)
