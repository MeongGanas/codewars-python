def nb_year(p0, percent, aug, p):
    # your code
    year = 0
    temp = p0
    while temp < p:
        temp = int(temp * (percent / 100 + 1) + aug)
        year += 1
    return year


print(nb_year(1500000, 0.25, 1000, 2000000))
