def tribonacci(signature, n):
    p1 = signature[:n]
    for i in range(n-len(signature)):
        p1.append(sum(p1[i:i+3]))
    return p1


print(tribonacci([0, 0, 1], 10))
print(tribonacci([0, 0, 0], 10))
print(tribonacci([3, 2, 1], 10))
print(tribonacci([1, 1, 1], 1))
print(tribonacci([1, 1, 1], 0))
print(tribonacci([1, 1, 1], 2))
