from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:

        return - (sqrt(discriminant) + b) / 2 * a, None

    else:
        return - (sqrt(discriminant) + b) / 2 * a, (sqrt(discriminant) - b) / 2 * a