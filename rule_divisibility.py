def thirt(n):
    # your code
    pattern = [1, 10, 9, 12, 3, 4]
    sum = 0

    while True:
        current_sum = 0
        for index, digit in enumerate(str(n)[::-1]):
            current_index = index % len(pattern)
            current_sum += int(digit) * pattern[current_index]

        if sum == current_sum:
            return sum

        sum = current_sum
        n = current_sum


array = [1, 10, 9, 12, 3, 4]


def thirt(n):
    total = sum([int(c) * array[i % 6]
                for i, c in enumerate(reversed(str(n)))])
    if n == total:
        return total
    return thirt(total)


print(thirt(1234567))
