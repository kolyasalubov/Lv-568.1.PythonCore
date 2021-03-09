even_list = []
odd_by_3_list = []
other_list = []

for x in range(1, 11):
    if x % 2 == 0:
        even_list.append(x)
    elif x % 3 == 0:
        odd_by_3_list.append(x)
    else:
        other_list.append(x)

print(even_list)
print(odd_by_3_list)
print(other_list)