import square
print("Select the desired shape for the calculation")
choice=input("If you want to calculate a triangle, enter 1, if circle 2 and rectangle 3:")
if choice=='1': #For circle
    print (square.circle(r=float(input("enter radius:"))))
elif choice=='2': #For rectangle
    print (square.rectangle(a=float(input("enter one side of the rectangle:")),
                                 b=float(input("enter the other side of the rectangle:"))))
elif choice=='3': #For triangle
    print(square.triangle(a=float(input("enter the length of the side of the triangle:")),
                          h=float(input("enter the height of the triangle:"))))
else:
    print ("mistake! Invalid input!")
    