#series.py

#def F():
#    a,b = 0,1
#    while True:
 #       yield a
 #       a, b = b, a + b

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

if __name__=='__main__':
    assert fibonacci(0) ==0
    assert fibonacci(1) ==1
    assert fibonacci(100) ==1
    print(fibonacci(18))
#from math import sqrt
#def F(n):
#    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

