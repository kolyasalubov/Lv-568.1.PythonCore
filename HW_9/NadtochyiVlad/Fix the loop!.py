def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + f'\n'
    return list

print(list_animals(["cat","dog"]))