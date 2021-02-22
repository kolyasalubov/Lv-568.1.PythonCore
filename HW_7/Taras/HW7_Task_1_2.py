import HW7_Task_1_1

print('''The square of ​​which figure you want to count?
1 - rectangle
2 - triangle
3 - circle''')
print('-' * 10)
choose = int(input('Enter the number: '))
print('-' * 10)

if choose == 1:
    height_rectangle = float(input('Enter the height of the rectangle: '))
    width_rectangle = float(input('Enter the width of the rectangle: '))
    print('-' * 10)
    HW7_Task_2_1.calc_rectangle(height_rectangle, width_rectangle)

elif choose == 2:
    length_triangle = float(input("Enter the length of the side of the triangle: "))
    height_triangle = float(input('Enter the height of the triangle: '))
    print('-' * 10)
    HW7_Task_2_1.calc_triangle(length_triangle, height_triangle)

elif choose == 3:
    radius = float(input('Enter the radius of the circle: '))
    print('-' * 10)
    HW7_Task_2_1.calc_circle(radius)
