first_value = int(input("Enter first value : "))
second_value = int(input("Enter second value : "))

print(f"First_value = {first_value} has id ", id(first_value))
print(f"Second_value = {second_value} has id ", id(second_value))

first_value,second_value = second_value,first_value

print(f"First_value = {first_value} has id ", id(first_value))
print(f"Second_value = {second_value} has id ", id(second_value))

print("The third variable was not used.")