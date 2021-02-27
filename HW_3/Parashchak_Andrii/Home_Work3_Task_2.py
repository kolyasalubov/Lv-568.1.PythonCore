num = int(input("Enter a four-digit number: "))
str_num = str(num)
list_num = list(str_num)

first_num = int(list_num[0])
second_num = int(list_num[1])
third_num = int(list_num [2])
fourth_num = int(list_num[3])

print(f"Multiplication of numbers {num} is ", first_num * second_num * third_num * fourth_num)
print(f"Reverse {num} is ", str_num[-1::-1])

sortednums = sorted(str_num)
print(f"Sort {num} is", sortednums)