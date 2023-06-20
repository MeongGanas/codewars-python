def remove_every_other(my_list):
    # Your code here!
    # return [my_list[i] for i in range(0, len(my_list), 2)]
    return my_list[::2]


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
