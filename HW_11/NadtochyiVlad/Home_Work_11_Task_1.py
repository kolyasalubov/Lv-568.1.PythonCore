def ever_or_odd_exeption(): 
    try:
        age_homo = int(input("Please enter your age : "))
        if age_homo > 0:
            if age_homo % 2 == 0:
                print("The age is odd")
            else:
                print("The age is even")
        else:
            raise ValueError("That is not positive number")

    except ValueError as e:
        print(e)
    except TypeError as e: 
        print(e)

ever_or_odd_exeption()