#!/usr/bin/env python3

def format_tuple(values):
    # ( 2, 123.4567, 10000, 12345.67)
    # Left pad
    print("file_{}".format("%03d" % values[0]))

    # Two decimal
    print("%.2f" % values[1])

    # Scientific notation
    print("{:.2e}".format(values[2]))
    print("{:.3e}".format(values[3]))


def formatter(values):
    fs = "the {} numbers are: "
    fs += ", ".join(["{}"] * len(values))
    print(fs.format(len(values), *values))


if __name__ == "__main__":
    format_tuple((2, 123.4567, 10000, 12345.67))
    formatter((1,2,3,4,5,6,7,8))
    formatter((1,2,3,4))
