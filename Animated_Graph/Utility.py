from math import sin, cos, tan


def cosec(x):
    return 1/(sin(x) + 0.00001)


def sec(x):
    return 1/(cos(x) + 0.00001)


def cot(x):
    return 1/(tan(x) + 0.00001)
