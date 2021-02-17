four_digit_number = int(input("Enter a four-digit number"))
str_four_digit_number= str(four_digit_number)
list_str_four_digit_number = list(str_four_digit_number)

first_number = int(list_str_four_digit_number[0])
second_number = int(list_str_four_digit_number[1])
third_number = int(list_str_four_digit_number[2])
fourth_number = int(list_str_four_digit_number[3])

print(f"The sum of the digits of this number {four_digit_number} is ", first_number+second_number+third_number+fourth_number)

print(f"Reverse the entered number {four_digit_number} is ", str_four_digit_number[-1::-1])

print(f"Sorting digits in a number {four_digit_number} is","".join(sorted(str_four_digit_number)))

