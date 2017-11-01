
'''
Fibonacchi recursion Python code

'''

# in-class (Chris's example):

'''
def fib(n):

	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n-1) + fib(n-2)

if __name__ == '__main__':
	assert fib(0) == 0
	assert fib(1) == 1
	assert fib(2) == 1
	assert fib(3) == 2
	print(fib(10))

'''

# the codes that I worked on after class: 

'''
## code 1:
def fibonacci(n, a=1, b=0):
    return b if n < 1 else fibonacci(n - 1, a + b, a)

print(fibonacci(7))
'''

## code 2:
class Program():

    def Fib(fib):
        if fib == 0:
            return 0
        elif fib == 1:
            return 1
        else:
            return Program.Fib(fib - 1 ) + Program.Fib(fib - 2)

print(Program.Fib(7))


'''
## code 3:

def fib(n):
    if n<2:
        return n
    else:
         return fib(n -1) + fib(n-2)
print(fib(7))
'''
