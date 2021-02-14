import math

def square_of_circle (radius):
    """
    function name square_of_figures
    input have one parameter: radius circle
    return : square circle  
    """
    square_circle = round(math.pi * pow(radius,2),2)
    return square_circle

def square_of_rectangle (length_rectangle, width_rectangle):
    """
    function name square_of_figures
    input have two parameters: length rectangle, width rectangle
    return : square rectangle 
    """
    square_rectangle = length_rectangle * width_rectangle
    return square_rectangle

def square_of_triangle (size_one, size_two, size_three):
    """
    function name square_of_figures
    input have three parameters: size_one triangle, size_two triangle, size_three triangle
    return : square triangle  
    """
    p = (size_one+size_two+size_three)/2 
    square_triangle = round(math.sqrt(p*(p-size_one)*(p-size_two)*(p-size_three)),2)
    return square_triangle

print(square_of_circle(2))
print(square_of_rectangle(4,2))
print(square_of_triangle(12,14,23))
