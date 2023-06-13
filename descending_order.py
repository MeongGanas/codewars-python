def descending_order(num):
    # Bust a move right here
    return int(''.join(sorted(list(str(num)), reverse=True)))


print(descending_order(5163))
