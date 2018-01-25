"""
Kathryn Egan
"""


def trapz(f, a, b):
    num_segments = 10
    segments = [f(value) for value in segment(a, b, num_segments)]
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
    def line2(x):
        return m * x + b
    return line2
