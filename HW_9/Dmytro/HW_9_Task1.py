def what_is_ur_age(age):
    if age < 0:
        raise ValueError("Ohhhh")
    elif age % 2 == 1:
        print("Your age is odd ", age)
    elif age % 2 == 0:
        print("Your age is even ", age)


try:
    what_is_ur_age(age=int(input("enter your age ")))
except ValueError as e:
    print(e)
