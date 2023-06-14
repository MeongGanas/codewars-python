def descending_order(num):
    # Bust a move right here

    # res = list(str(num))
    # for i in range(len(res)):
    #     for j in range(i + 1, len(res)):
    #         if res[i] > res[j]:
    #             res[i], res[j] = res[j], res[i]
    # return int(''.join(res[::-1]))

    return int(''.join(sorted(list(str(num)), reverse=True)))


print(descending_order(5163))
