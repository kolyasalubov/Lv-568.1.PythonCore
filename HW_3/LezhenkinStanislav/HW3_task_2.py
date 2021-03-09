four_digit_number = int(3562)
change_class = s = str(four_digit_number)
product_for_numbers = 1
for i in range (len(s)) :
    product_for_numbers*=int (s[i])

reverse = int(str(four_digit_number)[::-1])
sorting = sorted(change_class)

print("Reversed: ", reverse)
print ("Product of numbers =",product_for_numbers)
print("Sorting: ", sorting[0], sorting[1], sorting[2], sorting[3])