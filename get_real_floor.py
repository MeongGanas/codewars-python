def get_real_floor(n):
    # code here
    return n if n <= 0 else n-2 if n >= 13 else n-1
