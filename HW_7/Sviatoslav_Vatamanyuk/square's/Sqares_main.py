from squares import *

choice = (int(input("Listen here, you have three options: \n\t1)Calculate triangle's perimeter"
      "\n\t2)Calculate circle's perimeter "
      "\n\t3)Calculate rectangle's perimeter\n")))
if choice == 1:
    print(square_triangle(int(input("Enter triangle's side A ")), int(input("Enter triangle's side B ")),
                          int(input("Enter triangle's side C "))))
elif choice == 2:
    print(square_circle(float(input("Enter r of circle "))))
elif choice == 3:
    print(square_rectangle(int(input("Enter rectangle's side A ")), int(input("Enter rectangle's side B "))))
else:
    print("There is an error occurred. System is shutdowning")
