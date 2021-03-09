login = input("Enter your login:")
if login == "First":
    print("Hello, First")         
else:
    while True:
        print ("Login is not correct, please try again")
        login2 = input("Enter your login or `q` in order to exit:")
        if login2 == "q":
                print ("bye")
                break
        if login2 == "First":
                print("Hello, First")
                break