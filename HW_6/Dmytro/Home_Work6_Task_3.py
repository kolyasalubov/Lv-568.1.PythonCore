def count(string):
    """
    return: number of characters in string without spaces
    """
    return sum(len(x) for x in string.split())


print(count(input("Hi! \n")))
