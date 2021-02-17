def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        name += " plays banjo"
    else:
        name += " does not play banjo"
    return name
    
