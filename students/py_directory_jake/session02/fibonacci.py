def fibonacci(n):
    return sum_series(x)

def lucas(n):
    return sum_series(x,2,1)

def sum_series(x,x_0=0,x_1=1):
	if x == 0:
        return x_0
    elif x == 1:
        return x_1
    else:
        return sum_series(x-2,x_0,x_1)+sum_series(x-1,x_0,x_1)