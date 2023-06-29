def sum_digits(number):
    return sum(map(int, str(abs(number))))


print(sum_digits(10))
print(sum_digits(99))
print(sum_digits(-99))
