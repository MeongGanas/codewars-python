def points(games):
    # res = 0
    # for i in games:
    #     i = i.split(":")
    #     for j in range(0, len(i) - 1):
    #         if int(i[j]) > int(i[j+1]):
    #             res += 3
    #         elif int(i[j]) == int(i[j+1]):
    #             res += 1
    # return res

    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in games))


print(points(['1:0', '2:0', '3:0', '4:0', '2:1',
      '3:1', '4:1', '3:2', '4:2', '4:3']))
print(points(['1:1', '2:2', '3:3', '4:4', '2:2',
      '3:3', '4:4', '3:3', '4:4', '4:4']))
