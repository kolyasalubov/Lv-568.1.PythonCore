x = int(input("Enter your num "))
factorial = 1
if x <= 0:
    print(" You can not use negative numbers or 0")
else:
    for i in range(1, x+1):
        factorial = factorial*i
        print(factorial)
       
