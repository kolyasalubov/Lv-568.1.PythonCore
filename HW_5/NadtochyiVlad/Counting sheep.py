def count_sheeps(array1):
    sheep = 0
    for value in range(len(array1)):
        if array1[value]== True:
            sheep+=1


    return sheep