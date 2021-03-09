## Program that calculates the square of ​​a rectangle, triangle and circle

###################################################################################
# square of triangle (трикутник) = a * h 
# square of rectangle (прямокутника) = x * y
# square of circle (кола) = p(3.14) * r**2
###################################################################################

## Way #1 using functions:

def square_of_triangle (a, h):
    print (f'The square of triangle equals:', a*h)

def square_of_rectangle (x, y):
    print (f'The square of rectangle equals:', x*y)

def square_of_circle (r):
    print (f'The square of circle equals:', 3.14*r**2)

# We are asking a user to make a choice
choice = int(input ("What area do you want to calculate?  1-rectangle ; 2-triangle ; 3-circle : "))

# Choosing a necessary function
if choice == 1:
    a = int(input("Enter a base of a triangle: "))
    h = int(input("Enter a the height of a triangle: "))
    square_of_triangle (a, h)
elif choice == 2:
    x = int(input("Enter a length of a rectangle: "))
    y = int(input("Enter a width of a rectangle: "))
    square_of_rectangle (x, y)
elif choice == 3:
    r = int(input("Enter a radius of a circle: "))
    square_of_circle (r)


###################################################################################

## Way #2 using if elif:

# choice = int(input ("What area do you want to calculate?  1 - triangle; 2 - rectangle; 3 - circle: "))
# if choice == 1:
#     a = int(input("Enter a base of a triangle: "))
#     h = int(input("Enter a the height of a triangle: "))
#     print(f'The square of triangle equals:', a*h)
# elif choice == 2:
#     x = int(input("Enter a length of a rectangle: "))
#     y = int(input("Enter a width of a rectangle: "))
#     print(f'The square of rectangle equals:', x*y)
# elif choice == 3:
#     p = 3.14
#     r = int(input("Enter a radius of a circle: "))
#     r**=2
#     print(f'The square of circle equals:', p*r)

###################################################################################