from math import sqrt

def rectangle_sqr(a, b):
    """ Function return a square of rectangle """
    return a*b

def triangle_sqr(a, b, c):
    """ Function return a square of triangle """
    p = (a + b + c)/2
    return round(sqrt(p * ((p - a) * (p - b) * (p - c))), 2)

def circle_sqr(r):
    """ Function return a square of circle """
    return 3.14 * r**2

choice = input("Which square you want to count?")

if choice.lower() == "circle":
    radius = int(input("Set radius lenght"))
    print(f"Square of the circle is {circle_sqr(radius)} cm2")
elif choice.lower() == "triangle":
    side1 = int(input("Set first side"))
    side2 = int(input("Set second side"))
    side3 = int(input("Set third side"))
    print(f"Square of triangle is {triangle_sqr(side1, side2, side3)} cm2")
elif choice.lower() == "rectangle":
    side1 = int(input("Set first side"))
    side2 = int(input("Set second side"))
    print(f"Square of rectangle is {rectangle_sqr(side1, side2)} cm2")