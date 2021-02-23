## The program to check the validity of a password

rules= ("""Password creating rules:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
""")
print (rules)
import re

def entering (u_pas):
    print(u_pas)
    check_1=bool(5<len(u_pas)<17)
    check_2=bool(re.findall("[$#@]", u_pas))
    check_3=bool(re.findall("[0-9]", u_pas))
    check_4 = bool(re.findall("[a-zA-Z]", u_pas))
    ## Checking users password by all the rules
    if check_1 and check_2 and check_3 and check_4 == True:
        print("Your password was successfully saved")
    else:
        print("Something wrong! Please, read the rules and try to create a password again.")
        cont=input("Will you continue? yes / no : ")
        if cont =="yes":
            entering (input("Enter the password according our rules: "))
        else:
            pass

entering (input("Enter the password according our rules: "))
