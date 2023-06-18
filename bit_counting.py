def count_bits(n):
    return sum(map(int, list(bin(n)[2:])))


print(count_bits(1234))
print(count_bits(4))
print(count_bits(7))
print(count_bits(9))
print(count_bits(10))
