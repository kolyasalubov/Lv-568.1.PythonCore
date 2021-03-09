import Module1


user_choice = input("Square of which figure you want to count? triangle = t, rectangle = r, circle =c.")

if user_choice == "t":
    side = int(input("Enter side:"))
    heigh = int(input("Enter heigh:"))
    print(Module1.trianglesqr(side, heigh))
elif user_choice == "r":
    side1 = int(input("Enter side 1:"))
    side2 = int(input("Enter side 2:"))
    print(Module1.rectanglesqr(side1, side2))
elif user_choice == "c":       
    radius = int(input("Enter the radius:"))
    print(Module1.circlesqr(radius))
        
    
    