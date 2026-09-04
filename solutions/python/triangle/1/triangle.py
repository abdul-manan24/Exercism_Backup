def triangle(sides):
    if any(len == 0 for len in sides):
        return False
        
    a, b, c = sides
    is_triangle = (a + b >= c) and (b + c >= a) and (a + c >= b)
    return is_triangle
def equilateral(sides):
    if triangle(sides):
        a, b, c = sides
        is_equilateral = a == b == c == a
        return is_equilateral

    return False


def isosceles(sides):
    if triangle(sides):
        a, b, c = sides
        is_isosceles = (a == b) or (a == c) or (b == c)
        return is_isosceles

    return False


def scalene(sides):
    if triangle(sides):
        a, b, c = sides
        is_scalene = (a != b) and (b != c) and (c != a)
        return is_scalene

    return False
