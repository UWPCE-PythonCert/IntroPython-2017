"""
Kathryn Egan
"""


def trapz(f, a, b, *args, **kwargs):
    num_segments = 1000
    segments = [
        f(value, *args, **kwargs)
        for value in segment(a, b, num_segments)]
    area_sub1 = (b - a) / num_segments
    area_sub2 = (segments[0] + segments[-1]) / 2
    area_sub3 = sum(segments[1:-1])
    return area_sub1 * (area_sub2 + area_sub3)


def segment(a, b, num_segments):
    step = (b - a) / num_segments
    while a <= b:
        yield a
        a += step


def line(m=1, b=0):
    return polynomial(m, b)


def quadratic(A, B, C):
    return polynomial(A, B, C)


def polynomial(*coeffs):
    """ Returns function that calculates polynomial of x
    given arbitrary number of coefficients.
    """
    def calculate(x):
        powers = reversed(range(0, len(coeffs)))
        return sum(coeff * x ** power for coeff, power in zip(coeffs, powers))
    return calculate


