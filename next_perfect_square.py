import math


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sq = math.sqrt(sq)
    return int((sq + 1) * (sq + 1)) if sq == float(int(sq)) else -1


print(find_next_square(625))
