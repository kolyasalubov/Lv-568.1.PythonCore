import calculator

print("Hello, what is your figure?\n a - rectangle\n b - triangle\n c - circle")
figure = input("Enter: ").lower()

if figure == "a" or figure == "rectangle":
    print("Square of ​​a rectangle =", calculator.square_rectangle(int(input("Enter the smaller side : ")), int(input("Enter the larger side : "))))
elif figure == "b" or figure == "triangle":
    print("Square of ​​a triangle =", calculator.square_triangle(int(input("Enter one side : ")), int(input("Enter hight : "))))
elif figure == "c" or figure == "circle":
    print("Square of ​​a circle =", calculator.square_circle(int(input("Enter the radius : "))))
else:
    print("Error, please try again")
