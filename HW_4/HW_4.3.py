fib_limit = int(input("Enter the limit of fibonacci list"))

num1 = 0
num2 = 1
fib_num = num1 + num2

print(num1)

while fib_num <= fib_limit:
    print(fib_num)
    fib_num = num1 + num2
    num1 = num2
    num2 = fib_num
