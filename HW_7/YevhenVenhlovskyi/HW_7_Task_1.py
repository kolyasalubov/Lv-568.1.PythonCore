# Аsk a user to make a choice
choice = int(input ("What area do you want to calculate?  1-rectangle ; 2-triangle ; 3-circle : "))

import HW_7_Task_1_calculating

# Choose a necessary function
if choice == 1:
    a = int(input("Enter a base of a triangle: "))
    h = int(input("Enter a the height of a triangle: "))
    HW_7_Task_1_calculating.square_of_triangle (a, h)

elif choice == 2:
    x = int(input("Enter a length of a rectangle: "))
    y = int(input("Enter a width of a rectangle: "))
    HW_7_Task_1_calculating.square_of_rectangle (x, y)

elif choice == 3:
    r = int(input("Enter a radius of a circle: "))
    HW_7_Task_1_calculating.square_of_circle (r)

## below calculating from other file

# def square_of_triangle (a, h):
#     print (f'The square of triangle equals:', a*h)

# def square_of_rectangle (x, y):
#     print (f'The square of rectangle equals:', x*y)

# def square_of_circle (r):
#     import math
#     print (f'The square of circle equals:', round(math.pi*math.pow(r,2),2))
