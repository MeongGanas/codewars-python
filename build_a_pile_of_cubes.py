def find_nb(m):
    # your code
    total = 0
    i = 1
    while total < m:
        total += i**3
        if total == m:
            return i
        i += 1
    return -1


print(find_nb(1071225))
print(find_nb(4183059834009))
print(find_nb(24723578342962))
