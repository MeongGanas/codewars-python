import math


def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0


print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(25))
print(is_square(26))
