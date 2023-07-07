def define_suit(card):
    # Good luck
    return {"C": "clubs", "S": "spades", "D": "diamonds"}.get(card[-1], "hearts")
