print ('Select the desired shape for the calculation')
PI=3.14

def circle (r):
    """
    a function that calculates the area of ​​a circle
    """
    return ((r**2)*PI)

def rectangle ():
    """
    a function that calculates the area of ​​a rectangle
    """
    return a*b

def triangle():
    """
    a function that calculates the area of ​​a triangle
    """
    return 0.5*a*h
while True:
    choice=input("If you want to calculate a triangle, enter 1, if circle 2 and rectangle 3:")

    if choice=='1': #For triangle
        a=float(input("enter the length of the side of the triangle:"))
        h=float(input("enter the height of the triangle:"))
        print('area of ​​a triangle:',triangle())
        print("if you want to calculate more, select the desired shape or enter 'q' to finish")
        continue
    if choice=='3': #For rectangle
        a=float(input("enter one side of the rectangle:"))
        b=float(input("enter the other side of the rectangle:"))
        print ('area of ​​a rectangle:',rectangle())
        print ("if you want to calculate more, select the desired shape or enter 'q' to finish")
        continue 
    if choice=='2': #For circle
        print ('area of ​​a circle',circle(r=float(input("enter the radius:"))))
        print ("if you want to calculate more, select the desired shape or enter 'q' to finish")
        continue
    if choice=='q':
        print ("Goodbye)")
        break
    else:
        print ("mistake! Invalid input! enter one of the suggested digits or 'q' to complete")
        continue
