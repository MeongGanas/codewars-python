def data_reverse(data):
    # temp = []
    # for i in range(0, len(data), 8):
    #     temp.insert(0, (data[i:i+8]))
    # return [j for i in temp for j in i]

    res = []
    for i in range(len(data)-8, -1, -8):
        res.extend(data[i:i+8])
    return res

data3 = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
data4 = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
print(data_reverse(data3) == data4)
