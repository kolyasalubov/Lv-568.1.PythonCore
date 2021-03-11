'''Write a Python program to check the validity of a password (input from users).

Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
 '''
import re

print('Minimum length 6 characters.')
print('Maximum length 16 characters.')
print(
    '''At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$  # @].''')
password = str(input('Enter password: '))
if len(password) < 6:
    print('Enter more characters ')
    password = str(input('Enter password: '))
elif (len(password) >= 6 and len(password) <= 12 and re.findall(r'[A-Za-z]', password)
      and re.search(r'[A-Z]', password) and re.search(r'[0-9]', password)
      and re.search(r'[$#@]', password)):
    print('Password is valid')
elif len(password) > 12:
    print('You have entered a lot of characters. Re-enter:')
    password = str(input('Enter password: '))
else:
    print('You entered an incorrect password. Please enter correct password:  ')
    password = str(input('Enter password: '))
