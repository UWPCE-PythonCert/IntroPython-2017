
"""def fizzbuzz(n):
    for n in range(1,n+1):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)

print(__name__)
if __name__=="__main__":
    fizzbuzz(100)


def fizzbuzz(n):
    for n in range(1,n+1):
        if n % 15 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)

print(__name__)
if __name__=="__main__":
    fizzbuzz(100)
"""
def fizzbuzz(n):
    for n in range(1,n+1):
        output=""
        if n % 3 == 0:
            output += "Fizz"
        if n % 5 == 0:
            output += "Buzz"
        if not output:
            output = n
            print(output)

print(__name__)
if __name__=="__main__":
    fizzbuzz(100)