LETTER_LOW_SYMBOL = 'abcdefghijklmnopqrstuvwxyz'
LETTER_UP_SYMBOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBER_SYMBOL = '123456789'
CHARACTER_SYMBOL = '$#@'
MIN_LEN_PASSWORD = 6
MAX_LEN_PASSWORD = 16

all_symbol = LETTER_LOW_SYMBOL + LETTER_UP_SYMBOL + NUMBER_SYMBOL + CHARACTER_SYMBOL

def check_letter(entered_password):
    for letter in entered_password:
        if letter not in all_symbol:
            print('An unavailable character is entered')
            return False

    check_low = any(letter in entered_password for letter in LETTER_LOW_SYMBOL) 
    check_up = any(letter in entered_password for letter in LETTER_UP_SYMBOL) 
    if check_low == True and check_up == True:
        return True
    else:
        print('At least 1 letter between [a-z] and 1 letter between [A-Z]')
        return False

def check_number(entered_password):
    ckeck = any(letter in entered_password for letter in NUMBER_SYMBOL)
    if ckeck == True:
        return True
    else:
        print('At least 1 number between [0-9]')
        return False

def check_character(entered_password):
    ckeck = any(letter in entered_password for letter in CHARACTER_SYMBOL)
    if ckeck == True:
        return True
    else:
        print('At least 1 character from [$#@]')
        return False

def  ckeck_len_password(len_password):
    if len(len_password) < MIN_LEN_PASSWORD:
        print('Password is too short')
        False
    elif len(len_password) > MAX_LEN_PASSWORD:
        print('Password is too long')
        False
    else:
        return True

print('-' * 10)
print('''This programm check your password to validity.
Your password must be include:
- At least 1 letter between [a-z] and 1 letter between [A-Z]
- At least 1 number between [0-9]
- At least 1 character from [$#@]
- Minimum length 6 characters.
- Maximum length 16 characters''')

while True:
    print('-' * 10)
    user_password = input('Enter a password: ')
    if ckeck_len_password(user_password) == True:
        if check_letter(user_password) == True and check_number(user_password) == True and check_character(user_password) == True:
            print('Password is a validity')
            break
        else:
            print('Your password is invalid, please, change password')
