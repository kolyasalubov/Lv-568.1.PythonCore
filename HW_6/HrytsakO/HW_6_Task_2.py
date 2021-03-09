import math

def square_rectangle(x1, x2):
    square = x1 * x2
    return square

def square_triangle(a, b, c):
    p = (a + b + c) / 2
    square = (p * (p - a) * (p - b) * (p - c))
    return square

def square_circle(r):
    square = math.pi * r ** 2
    return square

print("Hello, what is your figure?\n a - rectangle\n b - triangle\n c - circle")
figure = input("Enter: ")

if figure == "a" or figure == "A":
    print("Square of ​​a rectangle =", square_rectangle(int(input("Enter the smaller side : ")), int(input("Enter the larger side : "))))
elif figure == "b" or figure == "B":
    print("Square of ​​a triangle =",square_triangle(int(input("Enter first side : ")), int(input("Enter second side : ")), int(input("Enter third side : "))))
elif figure == "c" or figure == "C":
    print("Square of ​​a circle =", square_circle(int(input("Enter the radius : "))))
else:
    print("Error, please try again")