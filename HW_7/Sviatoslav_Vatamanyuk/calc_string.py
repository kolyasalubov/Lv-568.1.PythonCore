def count_str(string):
    """
    func name is count_str
    :param string:
    :return: number of characters in string without spaces
    """
    return sum(len(x) for x in string.split())


print(count_str(input("Enter whatever u wanna\n")))

