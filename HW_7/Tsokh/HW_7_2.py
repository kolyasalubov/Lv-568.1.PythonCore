import re

user_password = input("Enter your password")

lower_case = re.findall("[a-z]", user_password)

upper_case = re.findall("[A-Z]", user_password)

special_symbol = re.findall("@|#|\$", user_password)


if not lower_case:
    print("Your password must contains one of this symbols [a-z]")

if not upper_case:
    print("Your password must contains one of this symbols [A-Z]")

if not special_symbol:
    print("Your password must contains one of this symbols [$, #, @]")

if len(user_password) >= 16 or len(user_password) <= 6:
    print("The length of password must be from 6 to 16 symbols")

else:
    print("Your password good enough")

