from math import sin, cos, tan

# + 0.00001 is there to avoid Zero-Division errors.
def cosec(x):
    return 1/(sin(x) + 0.00001)


def sec(x):
    return 1/(cos(x) + 0.00001)


def cot(x):
    return 1/(tan(x) + 0.00001)
