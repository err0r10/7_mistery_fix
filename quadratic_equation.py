from math import sqrt


def get_roots(a, b, c):
    '''
    Функция высчитывает дискриминант квадратного трехчлена.
    Возвращает корни квадратного уравнения x1 и x2
    '''
    discriminant = b ** 2 - 4 * a * c
    x1 = (sqrt(discriminant) + b) / 2 * a * (-1) if discriminant >= 0 else None
    x2 = (sqrt(discriminant) - b) / 2 * a if discriminant > 0 else None
    return x1, x2
