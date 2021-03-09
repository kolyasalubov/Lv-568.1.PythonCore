def rectangle(a, b):
    return int(a)*int(b)


def triangle(a, h):
    return int(a)*int(h)/2


def circle(r):
    from math import pi
    return pi*int(r)*int(r)


shape = input("Select a shape (triangle, circle or rectangle)")
if shape == "triangle" or shape == "Triangle":
    print(triangle(input("a = "), input("h = ")))
elif shape == "circle" or shape == "Circle":
    print(circle(input("r = ")))
elif shape == "rectangle" or shape == "Rectangle":
    print(rectangle(input("a = "), input("b = ")))
else:
    print("Error")
