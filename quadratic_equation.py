from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        r1 = (sqrt(discriminant) + b) / 2 * a * (-1)
        r2 = (sqrt(discriminant) - b) / 2 * a
        return r1, r2
    elif discriminant == 0:
        r1 = (sqrt(discriminant) + b) / 2 * a * (-1)
        return r1, None
    else:
        return None, None