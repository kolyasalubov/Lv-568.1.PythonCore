def are_you_playing_banjo(name):
    ''' function name are_you_playing_banjo
        input parametr: name
        split the string into characters
        check if the first character R or r return name + " plays banjo"
        elso return name + " does not play banjo
    '''
    st = list(name)
    if st[0] == 'R' or st[0] == 'r':
        return name + " plays banjo"
    return name + " does not play banjo"


a = str(input())

s = are_you_playing_banjo(a)
print(s)