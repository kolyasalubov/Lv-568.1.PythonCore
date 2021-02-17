list_len = int(input("Specify the number of items in the list :"))
print("List items must be integer.")
list_integer = []

for i in range(list_len):
    list_integer.append(int(input()))


print(f"A list that contains elements of integer type: {list_integer}")

for i in range(list_len):
    list_integer[i] = float(list_integer[i])

print(f"A list that contains elements of float type: {list_integer}")
