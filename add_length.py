def add_length(str_):
    # your code here
    return list(map(lambda x: f"{x} {len(x)}", str_.split()))


print(add_length("apple ler"))
