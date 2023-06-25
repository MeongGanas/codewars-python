def find_multiples(integer, limit):
    # Your code here!
    return [i for i in range(1, limit+1) if i % integer == 0]
