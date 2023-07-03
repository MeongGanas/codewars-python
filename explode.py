def explode(arr):
    num = list(filter(lambda x: type(x) == int, arr))
    return "Void!" if len(num) == 0 else [arr for i in range(sum(num))]
