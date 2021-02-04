number = int(input('Enter number: '))
res = 1
for factorial in range(1, number + 1):
    res *= factorial
print(res)