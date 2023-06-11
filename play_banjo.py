def are_you_playing_banjo(name):
    # Implement me!
    return name + (" plays banjo" if name[0].lower() == "r" else " does not play banjo")


print(are_you_playing_banjo("martin"))
print(are_you_playing_banjo("rartin"))
