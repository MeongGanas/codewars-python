def reverse_letter(string):
    # do your magic here
    return ''.join([i for i in string if i.isalpha()][::-1])
