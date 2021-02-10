while True:
    login = input("Enter your login")
    if login == "First":
        print("Greetings, First")
    else:
        print("Error, wrong login")
    again = input("Try again?")
    if again in ["Yes", "yes", "Y", "y"]:
        continue
    else:
        break