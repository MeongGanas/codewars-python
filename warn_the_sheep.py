def warn_the_sheep(queue):
    sheep = len(queue) - queue.index("wolf") - 1
    return "Oi! Sheep number {}! You are about to be eaten by a wolf!".format(sheep) if sheep > 0 else "Pls go away and stop eating my sheep"
