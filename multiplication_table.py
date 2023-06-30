def multiplication_table(size):
    # res = []
    # for i in range(1, size+1):
    #     temp = []
    #     for j in range(1, size+1):
    #         temp.append(i*j)
    #     res.append(temp)
    # return res

    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]


print(multiplication_table(2))
