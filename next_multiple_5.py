def round_to_next5(n):
    # Your code here
    while n % 5 != 0:
        n += 1
    return n


print(round_to_next5(12))
