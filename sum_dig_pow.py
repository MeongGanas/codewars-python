def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    # your code here
    return [i for i in range(a, b+1)
            if sum(int(v) ** i for i, v in enumerate(str(i), 1)) == i]


print(sum_dig_pow(1, 100))
print(sum_dig_pow(925, 2683))
