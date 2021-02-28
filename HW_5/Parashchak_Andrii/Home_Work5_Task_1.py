even_nums_devisible_by_2 = []

for nums in range(1,11):
    if nums % 2 == 0:
        even_nums_devisible_by_2.append(nums)
print("Even numbers that are divisible by 2:", even_nums_devisible_by_2)

odd_nums_devisible_by_3 = []

for nums in range(1,11):
    if nums % 3 == 0:
        odd_nums_devisible_by_3.append(nums)
print("Odd numbers that are divisible by 3: ", odd_nums_devisible_by_3)

nums_not_devisible_by_2_3 = []
for nums in range(1,11):
    if nums % 3 != 0 and nums % 2 != 0:
        nums_not_devisible_by_2_3.append(nums)
print("Nums not devisible by 2 3: ", nums_not_devisible_by_2_3)

