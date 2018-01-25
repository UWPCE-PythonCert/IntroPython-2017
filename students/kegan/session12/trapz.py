"""
Kathryn Egan
"""


def trapz(f, a, b, *args, **kwargs):
    """ Returns the area under the given function f between
    points a and b.
    Args:
        f (function) : function to compute
        a (num) : start point
        b (num) : end point
    Returns:
        float : area under f between a and b
    """
    num_segments = 1000
    segments = [
        f(value, *args, **kwargs)
        for value in segment(a, b, num_segments)]
    area_sub1 = (b - a) / num_segments
    area_sub2 = (segments[0] + segments[-1]) / 2
    area_sub3 = sum(segments[1:-1])
    return area_sub1 * (area_sub2 + area_sub3)


def segment(a, b, num_segments):
    """ Generator yielding segments between a and b (inclusive)
    according to the number of segments requested.
    Args:
        a (num) : start point
        b (num) : end point
        num_segments (int) : number of segments between a and b to yield
    """
    step = (b - a) / num_segments
    while a <= b:
        yield a
        a += step


def line(m=1, b=0):
    """ Returns function for line with given slope and intercept. """
    return polynomial(m, b)


def quadratic(A, B, C):
    """ Returns quadratic function for coefficients A, B, and C. """
    return polynomial(A, B, C)


def polynomial(*coeffs):
    """ Returns polynomial function for arbitrary number of coefficients. """
    def calculate(x):
        powers = reversed(range(0, len(coeffs)))
        return sum(coeff * x ** power for coeff, power in zip(coeffs, powers))
    return calculate
