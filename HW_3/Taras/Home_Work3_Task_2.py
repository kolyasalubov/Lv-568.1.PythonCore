number = int(input('Enter number(4): '))

str_number = str(number)

print('Product of numbers: ' + str(int(str_number[0]) * int(str_number[1]) * int(str_number[2]) * int(str_number[3])))

print('Revers: ' + str_number[::-1])

print('Sorted: ' + str(int(''.join(sorted(str_number)))))