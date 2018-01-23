def trapz(fun, a, b):
    '''
    Trapezoidal Function
    '''
    x_values = [i for i in range(1,101)]

    area1 = (b - a)/(2 * len(x_values))
    area2 = fun(x_values[0]) + fun(x_values[-1])
    area3 = 2 * sum(fun(x) for x in x_values[1:-1])
    tot_area = area1 * (area2 + area3)
    return tot_area
