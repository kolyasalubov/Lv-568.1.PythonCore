def largest_of_number(arg1, arg2):
    '''function returns the largest number of two numbers '''
    if arg1 >= arg2:  
        return arg1 
    elif arg1 < arg2: 
        return arg2
    
largest_of_number(int(input('Enter first number: ')), int(input('Enter second number: ')))
