def max_number (*numbers):
    """
    function that returns the largest number of two numbers
    """
    return max(numbers) 
print((max_number.__doc__),'largest number:',(max_number
                                             (float(input("Enter first number: ")),
                                             float(input("Enter second number: ")))))

#print (max_number.__doc__, 'largest number:',max_number(55,66))
