fib1 = fib2 = 1

n = int(input('Enter item number: '))

if n < 2:
    quit()

print(fib1, end=' ')
print(fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

print()