import math

def rectangle (side_one, side_two):
    """
    function name rectangle
    input parametrs two: side_one , side_two
    return area rectangle
    """
    return side_one*side_two

def triangle (height, side):
    """
    function name triangle
    input parametrs two: height , side_to_height
    return area triangle
    """
    return 0.5*height*side

def circle (radius):
    """
    function name circle
    input parametr: radius
    return area circle
    """
    return round(math.pow(math.pi*radius,2),2)
