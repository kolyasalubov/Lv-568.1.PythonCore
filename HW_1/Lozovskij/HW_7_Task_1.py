choice = int(input ("What area do you want to calculate?  1-rectangle ; 2-triangle ; 3-circle : "))
import HW_6_Task_2

if choice == 1:
    a = int(input("Enter a base of a triangle: "))
    h = int(input("Enter a the height of a triangle: "))
    HW_6_Task_2.square_of_triangle (a, h)

elif choice == 2:
    x = int(input("Enter a length of a rectangle: "))
    y = int(input("Enter a width of a rectangle: "))
    HW_6_Task_2.square_of_rectangle (x, y)

elif choice == 3:
    r = int(input("Enter a radius of a circle: "))