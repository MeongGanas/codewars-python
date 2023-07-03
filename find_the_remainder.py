def remainder(a, b):
    # your code here
    try:
        return a % b if a > b else b % a
    except:
        return None
