def largest_return(x1, x2):
    """
    function name largest_return
    input parametres two: x1, x2
    returns the largest number of two numbers
    """
    if x1 > x2:
        return x1
    elif x1 < x2:
        return x2
    
print(largest_return(505, 88))