try:    
    days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}

    choice = int(input("Enter a number of day"))
    
    if choice not in [1, 2, 3, 4, 5, 6, 7]:
        raise ValueError("Numbers should be in [1, 2, 3, 4, 5, 6, 7]")
    else:
        print(days[choice])
except ValueError as e:
    print(e)