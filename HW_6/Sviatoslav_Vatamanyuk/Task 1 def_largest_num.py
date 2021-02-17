# def larger(arg1, arg2):
#     """
#     func name ms larger
#     input two args
#     return greater number
#     """
#     if arg1 > arg2:
#         print("First num larger and is = ", arg1)
#     if arg2 > arg1:
#         print("Second num larger and is = ", arg2)
#     else:
#         print("Numbers are equal")
#
#
# larger(input("First num "), input("Second "))

def larger(arg1, arg2):
    """
    func name is larger
    input two args
    returns larger num
    """
    return max(arg1, arg2)
print(larger(input("First num "), input("Second num ")))

