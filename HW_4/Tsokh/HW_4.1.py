factorial_number = int(input("Enter a number to determine factorial"))
if factorial_number < 0:
    print("You can't  determine factorial from egative number. Please enter positive one or 0")
    factorial_number = int(input("Enter a number to determine factorial"))

if factorial_number == 0:
    print("Factorial of 0 = 1")
else:
    factorial_number = range(1, factorial_number + 1)

    factorial = 1

    x = 0

    while x < len(factorial_number):
        factorial = factorial_number[x]*factorial
        x += 1

    print(f"Factorial of {len(factorial_number)} = {factorial}")
