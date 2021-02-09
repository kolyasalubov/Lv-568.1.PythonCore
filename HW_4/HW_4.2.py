list_limit = int(input("Enter the list limit"))
int_list = list(range(list_limit + 1))

i = 0

float_list = []

for x in int_list:
    float_list.append(float(int_list[i]))
    i += 1

print(float_list)