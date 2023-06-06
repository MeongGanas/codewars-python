def rps(p1, p2):
    hand = {"rock": 0, "paper": 1, "scissor": 2}
    results = ["Draw!", "Player 1 won!", "Player 2 won!"]
    return results[hand[p1] - hand[p2]]


print(rps("scissor", "paper"))
