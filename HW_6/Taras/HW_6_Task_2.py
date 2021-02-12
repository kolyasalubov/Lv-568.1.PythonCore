PI = 3.14

def rectangl(arg1, arg2):
    print('The square of ​​the rectangle is equal to: ', round(arg1 * arg2, 3))

def equilateral_triangle(arg):
    print('The square of ​​the equilateral triangle is equal to: ', round(arg**2 * 3**0.5 / 4, 3))

def right_triangle(arg1, arg2):
    print('The square of ​​the right triangle is equal to: ', round(1 / 2 * arg1 * arg2, 3))

def circle(arg):
    print('The square of ​​the circle is equal to: ', round(PI * arg**2, 3))

print('The square of ​​which figure you want to count?')
print('1 - rectangl')
print('2 - equilateral_triangle')
print('3 - right_triangle')
print('4 - circle')
print('-' * 10)
choose = int(input('Enter the number of figure: '))
print('-' * 10)

if choose == 1:
    height_rectangl = float(input('Enter the height of the rectangle: '))
    width_rectangl = float(input('Enter the width of the rectangle: '))
    print('-' * 10)
    rectangl(height_rectangl, width_rectangl)

elif choose == 2:
    length_triangle = float(input("Enter the length of the side of the triangle: "))
    print('-' * 10)
    equilateral_triangle(length_triangle)

elif choose == 3:
    first_leg = float(input('Enter the length of the first leg: '))
    second_leg = float(input('Enter the length of the second leg: '))
    print('-' * 10)
    right_triangle(first_leg, second_leg)

elif choose == 4:
    radius = float(input('Enter the radius of the circle: '))
    print('-' * 10)
    circle(radius)