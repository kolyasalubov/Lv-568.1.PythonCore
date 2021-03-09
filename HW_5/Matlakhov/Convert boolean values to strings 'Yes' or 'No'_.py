def bool_to_word(boolean):
    ''' function name bool_to_word
        input parametr: boolean
        if the value is True then return 'Yes' else return 'No'
    '''
    if str(boolean) == 'True':
        return 'Yes'
    return 'No'


d = bool_to_word('True')
print(d)
