def count_sheeps(sheep):
    '''function name count_sheeps
        input parametr: sheep
        compare the value with True
        count the values True 
        return count i
    '''
    i = 0
    for x in sheep:
        if x == True:
            i += 1
    return i


p = count_sheeps([True,  True,  True,  False,
                  True,  True,  True,  True,
                  True,  False, True,  False,
                  True,  False, False, True,
                  True,  True,  True,  True,
                  False, False, True,  True])
print(p)
