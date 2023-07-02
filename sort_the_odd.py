# def sort_array(source_array):
#     # Return a sorted array.
#     odd = sorted([i for i in source_array if i % 2 == 1])
#     index = 0
#     for i in range(len(source_array)):
#         if source_array[i] % 2 == 1:
#             source_array[i] = odd[index]
#             index += 1
#     return source_array

def sort_array(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


print(sort_array([5, 3, 2, 8, 1, 4]))
