def delete_nth(order, max_e):
    # code here
    ans = []
    for o in order:
        if ans.count(o) < max_e:
            ans.append(o)
    return ans


print(delete_nth([20, 37, 20, 21], 1))
print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))
