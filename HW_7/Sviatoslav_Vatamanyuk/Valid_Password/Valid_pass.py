login = str(input("Please enter your password \n"))


if login.islower() or login.isalnum():
    print("Your password suppose to have at least one uppercase letter, special character and number \n")
    login = str(input("Please enter valid password "))
elif login.isdigit():
    if len(login) < 6 or len(login) > 16:
        print('Password is not valid \n')
        login = str(input("Please enter valid password "))

print("Your password is ", login)
