def tower_builder(n_floors):
    # build here
    return [" "*(n_floors-1-i) + "*" * (2*i+1) + " " * (n_floors-1-i)
            for i in range(n_floors)]


print(tower_builder(2))
print(tower_builder(3))
print(tower_builder(6))
