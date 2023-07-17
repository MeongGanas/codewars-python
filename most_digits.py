def find_longest(arr):
    # your code here
    maximum = ""
    for number in arr:
        number = str(number)
        if len(number) > len(maximum):
            maximum = number
    return int(maximum)
