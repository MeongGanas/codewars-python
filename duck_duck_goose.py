def duck_duck_goose(players, goose):
    # ...
    pos = goose % len(players)
    return players[pos-1].name
