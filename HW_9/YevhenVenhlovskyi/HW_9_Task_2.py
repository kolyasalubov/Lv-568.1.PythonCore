## HW_9_Task_2 Relation of days of the week to entered numbers

def handling_rel (number):
    print (f'The {number} day of the week is {relation[number]}')

relation={1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}

try:
    number=int(input('Enter a number of the week from 1 to 7: '))
except (TypeError, ValueError):
    print ("Entered number is not valid")
else:
    if number > 7:
        raise Exception ("Sorry, entered number over 7")
    if number == 0:
        raise Exception ("Sorry, entered number equals zero")
    else:
        handling_rel (number)
