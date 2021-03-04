## HW_9_Task_1 Checking user's age

## Check the entered number: even or odd
def number_check (x):
    if x%2 != 0 :
        print(f'{x} is odd')
    else:
        print(f'{x} is even')

## Entering age
y=int(input("Please, enter your age: "))

## Handling exceptions
if y < 0:
  raise Exception("Sorry, entered numbers below zero")

## Call the check function
number_check(y)

