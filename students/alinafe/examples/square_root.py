"""
http://greenteapress.com/thinkpython/html/thinkpython008.html
excercise 2
Encapsulate this loop in a function called square_root that takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a.
"""
n = raw_input('Square root of what?\n')
 
def square_root(n):
   n = float(n) # Convert to float 
   x = n / 2     # rough estimate of sqrt, half the input
   i = 0           # initialize counter
   while i < 10: 
       y = (x + n / x) / 2 
       x = y                      
       i += 1  # increment counter by 1 each iteration
   print x
 
square_root(n)
