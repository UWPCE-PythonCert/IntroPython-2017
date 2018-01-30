def quadratic(x, A=0, B=0, C=0):
    return A * x**2 + B * x + C

def trapz(fun, a, b, *args, **kwargs):
    '''
    Trapezoidal Function
    '''

    # The next four lines are generating 100 evenly distributed 
    # x coordinates between points a and b
    x_values = []
    x_values.append(a+((b-a)/100))
    for i in range(1,101):
        x_values.append(x_values[i-1]+((b-a)/100))

#    if hasattr(coef):
#        text = 'Has coef attribute'
#        return text

    area1 = (b - a)/(2 * len(x_values))
    area2 = fun(x_values[0], *args, **kwargs) + fun(x_values[-1], *args, **kwargs)
    area3 = 2 * sum(fun(x, *args, **kwargs) for x in x_values[1:-1])
    tot_area = area1 * (area2 + area3)
    return tot_area
