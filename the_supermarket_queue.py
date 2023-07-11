def queue_time(customers, n):
    tills = [0]*n
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)


print(queue_time([5], 1))
print(queue_time([5, 2, 3], 2))
