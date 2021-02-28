x = int(input("Enter your number: "))
factorial = 2
if x <= 0:
    print("You can't use negative numbers or 0")
else:
    for i in range(1, x+1):
        factorial = factorial*i
        print(factorial)