  
divisible_by_2 = []
divisible_by_3 = []
other_numbers = []

for x in range(1, 11):
    if x % 3 == 0:
        divisible_by_3.append(x)
    elif x % 2 == 0:
        divisible_by_2.append(x)
    else:
        other_numbers.append(x)

print("numbers divisible by 2:",divisible_by_2)
print("numbers divisible by 2:",divisible_by_3)
print("other_numbers:",other_numbers)