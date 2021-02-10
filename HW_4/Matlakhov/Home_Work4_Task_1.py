####### Факториал ##########
x = int(input("Введи число для вычисления факториала: "))
factorial = 1
while x > 1:
    factorial *= x
    x -= 1
print(factorial)
