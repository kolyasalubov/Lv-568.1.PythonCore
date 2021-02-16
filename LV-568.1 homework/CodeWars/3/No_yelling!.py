def filter_words(st):
    """
    Func name is filter_words
    :param st:
    :return: Capital and without spoiled spaces
    """
    return ' '.join((st.capitalize()).split())


print(filter_words("PYCHARM    could not make PROPERLY   spaCEd  StRiNg"))