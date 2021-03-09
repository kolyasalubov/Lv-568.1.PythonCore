def f_words(s):
    '''function name f_words
        input string: s
        change the first letter to capital
        return the result
    '''
    return s[0].upper() + s.lower()[1:]


a = f_words('hEllow Word')
print(a)
