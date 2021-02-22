def square_circle(r):
    """
    function = square_circle
    :param r:
    :return: P
    """
    P = 2 * 3.14 * r
    return "The square of circle is ", P


def square_triangle(argA, argB, argC):
    """
    func is square_triangle
    :param argA:
    :param argB:
    :param argC:
    return: P
    """
    P = argA + argB + argC
    return "The square of triangle is ", P


def square_rectangle(argA, argB):
    """
    func is sqare_rectangle
    :param argA:
    :param argB:
    :return: P of rectangle
    """
    return "The square of rectangle is ", (argA + argB) * 2


"""   entering all arguments and calling functions   """

#
# print(square_circle(float(input("Enter r of circle "))))
# print(square_triangle(int(input("Enter triangle's side A ")), int(input("Enter triangle's side B ")),
#                       int(input("Enter triangle's side C "))))
# print(square_rectangle(int(input("Enter rectangle's side A ")), int(input("Enter rectangle's side B "))))
