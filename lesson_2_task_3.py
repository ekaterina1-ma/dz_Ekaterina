import math


def square(side):
    result = side * side
    if not isinstance(side, int):
        return math.ceil(result)
    else:
        return result


side1 = 14
result1 = square(side1)
print(f"Площадь квадрата со стороной {side1} = {result1}")
