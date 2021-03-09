def NumberOfCharacters(*args):
    return len(*args)

def NumberOfCharactersSet(*args):
    return len(set(*args))

print(NumberOfCharacters("ggdgfdbbbbbbd32"))
print(NumberOfCharactersSet("ggdgfdbbbbbbd32"))