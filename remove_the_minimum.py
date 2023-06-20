def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    working_num = numbers.copy()
    working_num.remove(min(working_num))
    return working_num


print(remove_smallest([1, 2, 3, 4, 5]))
