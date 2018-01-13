
""" Functions that return Nth entry of a sum sequence. """

def sum_series(nth=1,sequence=[0,1]):
    """ Generate a list of sums given a seed and return the Nth number. """
    for i in range(2, nth):
        sequence.append(sequence[i-2]+sequence[i-1])
    return sequence[nth-1]

def fibonacci(n):
    """ Return the Nth Fibonacci number. """
    return sum_series(n,[0,1])
    #for i in range(2, n):
    #    series.append(series[i-2]+series[i-1])
    #print(series)
    #return series[n-1]

def lucas(n):
    """ Return the Nth Lucas number. """
    return sum_series(n,[2,1])

def tests():
    """ Sanity check the functions. """

    # verify the fibonacci calculations are operating correctly
    assert fibonacci(1)==0, "Fibonacci computation malfunctioning!"
    assert fibonacci(4)==2, "Fibonacci computation malfunctioning!"
    assert fibonacci(20)==4181, "Fibonacci computation malfunctioning!"
    #assert fibonacci(20)==481, "Fibonacci computation malfunctioning! (TEST)"

    # verify the lucas calculations are operating correctly
    assert lucas(1)==2, "Lucas computation malfunctioning!"
    assert lucas(5)==7, "Lucas computation malfunctioning!"
    assert lucas(8)==29, "Lucas computation malfunctioning!"
    #assert lucas(8)==9, "Lucas computation malfunctioning! (TEST)"

    # verify the generic computation function

    # verify function properly defaults to fibonacci sequence behavior
    assert sum_series(20)==4181, "Generic series computation malfunctioning!"
    # verify non lucas and fibonacci sequences operate correctly
    assert sum_series(3,[2,2])==4, "Generic series computation malfunctioning!"
    #assert sum_series(3,[2,2])==7, "Generic series computation malfunctioning! (TEST)"


# sanity test the functions
tests()

print(fibonacci(20))
