def square_digits(num):
    # Your code here
    return int(''.join([str(int(i) * int(i)) for i in list(str(num))]))


print(square_digits(9119))
