
print("Выбирите необходимую фигуру")


def triangle(a, h):
    """ function name triangle
        input parametrs two: side length a, height h
        calculates the square of ​​a triangle 
        return square of ​​a triangle
    """
    st = 0.5 * a * h
    return st


def rectangle(a, b):
    """ function name rectangle
        input parametrs two: length a, and width b
        calculates the square of ​​a rectangle 
        return square of ​​a rectangle
    """
    sr = a * b
    return sr


def circle(r):
    """ function name circle
        input parametr one: circle radius r and constant
        calculates the square of ​​a circle
        return square of ​​a circle
    """
    sc = 3.14 * r ** 2
    return sc


x = int(input("Если трехугольник введи - 1; Прямоугольника - 2; Круг - 3: "))

if x == 1:
    a = float(input("Укажи длину стороны треугольника: "))
    h = float(input("Укажи высоту треугольника: "))
    sqt = triangle(a, h)
    print(sqt)
elif x == 2:
    a = float(input("Укажи длину стороны прямоугольника: "))
    b = float(input("Укажи ширину прямоугольника: "))
    sqr = rectangle(a, b)
    print(sqr)
elif x == 3:
    r = float(input("Укажи радиус круга: "))
    sqc = circle(r)
    print(sqc)
else:
    print("Вы выбрали не правильную фигуру")
    print("Выбирите необходимую фигуру")
    x = int(input("Если трехугольник введи - 1; Прямоугольника - 2; Круг - 3: "))

# w=triangle(4, 7)
# print(w)
