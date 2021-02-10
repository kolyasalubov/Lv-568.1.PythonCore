print('even number that are divisible by 2: ', end = ' ')
for number in range(1, 10):
    if number % 2 == 0:
        print(number, end = ' ')
print()
print('odd number, which are divisible by 3: ', end = ' ')
for number_2 in range(1, 10):
    if number_2 % 2 != 0 and number_2 % 3 == 0:
        print(number_2, end = ' ')
print()
print('number that are not divisible by 2 and 3: ', end = ' ')
for number_3 in range(1, 10):
    if number_3 % 2 != 0 and number_3 % 3 != 0:
        print(number_3, end = ' ')
print()