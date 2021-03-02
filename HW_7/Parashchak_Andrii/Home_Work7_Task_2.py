import re
while True:
    password=input("Enter password:")
    if bool(5<len(password)<17)==False:
        print("mistake!the password must be between 6 and 16 characters long")
        continue
    elif bool(re.findall("[$#@]", password))==False:
        print ("password must contain at least 1 character with [$ # @]")
        continue
    elif bool(re.findall("[0-9]", password))==False:
        print ("mistake! password must contain at least 1 digit and 0 to 9")
        continue
    elif bool(re.findall("[A-Z]", password))==False:
        print("mistake! password must contain at least 1 uppercase and 1 lowercase letter ")
        continue
    elif bool(re.findall("[a-z]", password))==False:
        print("mistake! password must contain at least 1 uppercase and 1 lowercase letter ")
        continue
    else:
        print ("Congratulations! you have successfully registered")
        break