from math import sqrt


def solve(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        print("no solutions ")
    elif d == 0:
        x = -b / (2*a)
        print("One solution " + str(x))
    elif d > 0:
        x1 = (-b + (sqrt(d)) / (2*a))
        x2 = (-b - (sqrt(d)) / (2*a))
        print("Two solutions " + str(x1) + "end " + str(x2))
    else:
        print("LOL_KEK_CHEBUREK!!!")


solve(1, 1, 1)
solve(1, 2, 1)
solve(1, 5, 6)
