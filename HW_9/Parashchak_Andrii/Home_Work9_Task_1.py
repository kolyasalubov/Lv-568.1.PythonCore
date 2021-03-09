try:
    age = int(input("Please enter your age"))
    if age < 0:
        raise ValueError("Age can't be negative")
    else:
        if age % 2 == 0:
            print("Age is even")
        else:
            print("Age is odd")

except ValueError as e:
    print(e)