## The program that calculates a square of ​​rectangle, triangle and circle

###################################################################################
# square of triangle (трикутник) = a * h
# square of rectangle (прямокутника) = x * y
# square of circle (кола) = p(3.14) * r**2
###################################################################################

def square_of_triangle (a, h):
    print (f'The square of triangle equals:', a*h)

def square_of_rectangle (x, y):
    print (f'The square of rectangle equals:', x*y)

def square_of_circle (r):
    import math
    print (f'The square of circle equals:', round(math.pi*math.pow(r,2),2))
