factorial_number = int(input("Enter a number to determine its factorial : "))
factorial_value= 1

if factorial_number == 0 :
    print(f"Factorial of your number is 1 .")
else:
    for i in range(1,factorial_number+1):
        factorial_value*= i

    print(f"Factorial of your number is {factorial_value} .")

