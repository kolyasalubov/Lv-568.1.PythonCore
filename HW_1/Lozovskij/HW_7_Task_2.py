import re
password = input("Enter your password: ")
if re.findall("[a-z]", password) == []:
    print("At least 1 letter between [a-z]")
elif re.findall("[A-Z]", password) == []:
    print("At least 1 letter between [A-Z]")
elif re.findall (r"\d", password) == []:
    print("At least 1 number between [0-9]")
elif re.findall("[$ # @]", password) == []:
    print("At least 1 character from [$#@]")
elif len(password) <= 6 or len(password) >= 16:
    print("Minimum length 6 characters and maximum length 16 characters")
else:
    print("secure password")