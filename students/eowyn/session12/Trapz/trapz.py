def xaxis(a, b, n):
    ''' Generate floating x-points from a to b, inclusive '''
    interval = (b - a) / n
    while a <= b:
        yield a
        a += interval


def trapz(fun, a, b):
    """
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes a single parameter

    :param a: the start point for the integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value
    """
    n = 1000
    deltax = (b - a) / n
    endpointssum = (fun(a) + fun(b)) / 2.0
    xpoints = [x for x in xaxis(a, b, n)]
    ypoints = [fun(x) for x in xpoints[1:-1]]  # excludes end points
    area = deltax * (endpointssum + sum(ypoints))

    return area



def get_curve(fun, *args, **kwargs):
    ''' Pass arguments to form of function to get the curve f(x) '''
    def curve(x):
        return fun(x, *args, **kwargs)
    return curve


def trapzargs(fun, a, b, *args, **kwargs):
    ''' Construct f(x) and calculate area under curve between a & b '''
    somefunc = get_curve(fun, *args, **kwargs)
    return trapz(somefunc, a, b)




