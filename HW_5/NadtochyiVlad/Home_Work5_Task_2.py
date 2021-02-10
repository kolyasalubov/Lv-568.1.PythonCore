user_login = input("Please enter login: ")

while user_login != "First":
    user_login = input("Incorrect login.\nPlease enter login: ")


print(f"Hello, {user_login}!")