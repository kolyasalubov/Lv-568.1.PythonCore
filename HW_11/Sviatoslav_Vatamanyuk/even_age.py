def what_is_ur_age(arg):
    try:
        if arg < 0:
            raise ValueError("How dare are you?")
        if arg % 2 == 0:
            print("Your age is odd ---> ", arg)
        elif arg % 2 == 1:
            print("Your age is even ---> ", arg)
        else:
            print("Error 404")
    except ValueError as e:
        print(e)


what_is_ur_age(arg=int(input("enter your age, pls ")))
