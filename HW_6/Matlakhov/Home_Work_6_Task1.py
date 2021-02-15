# print("Введи два значения")
# a = int(input("Веди первое значение: "))
# b = int(input("Веди второе значение: "))


# def f1(arg1, arg2):
""" function name f1
        input parametrs two: arg1, arg2
        determine the maximum value
        return the maximum value
    """
#     max1 = max(arg1, arg2)
#     return max1


# maxi = f1(a, b)
# print(maxi)

#######################
# def f1(arg1, arg2):
""" function name f1
        input parametrs two: arg1, arg2
        determine the maximum value
        return the maximum value
    """
#     max1 = max(arg1, arg2)
#     return max1


# maxi = f1(15, 17)
# print(maxi)


######################

x = int(input("Сколько эллементов будет: "))
l = []
i = 0
while i < x:
    a = int(input("Введи следующее число: "))
    l.append(a)
    i += 1
print(l)


def f1(*arg):
    """ function name f1
        input parametrs 
        determine the maximum value
        return the maximum value
    """
    max1 = max(*arg)
    return max1


maxi = f1(l)
print(maxi)
