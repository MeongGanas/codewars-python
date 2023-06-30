def race(v1, v2, g):
    # your code
    if v1 >= v2:
        return None
    time = g * 3600 / (v2 - v1)
    return list(map(int, [time/3600, (time % 3600) / 60, time % 60]))


print(race(720, 850, 70))
print(race(80, 91, 37))
