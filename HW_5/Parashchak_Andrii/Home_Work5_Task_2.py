name = input("Whats your name? ")
login = input("Enter you login: ")

while login == "first":
    print("Hello", name)
    if login == "first":
        break
else:
    print("Error")