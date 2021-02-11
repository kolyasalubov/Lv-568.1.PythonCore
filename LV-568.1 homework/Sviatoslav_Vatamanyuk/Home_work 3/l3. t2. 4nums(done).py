number = input('Enter your number: ')
number_list = list(number)
number_product = int(number_list[0]) * int(number_list[1]) * int(number_list[2]) * int(number_list[3])
number_reversed = number_list[::-1]
print(f'Your reversed number:', number_reversed)
print (f'Your product number:', number_product)
number_sorted = sorted(number)
print("Your sorted number is ", number_sorted)