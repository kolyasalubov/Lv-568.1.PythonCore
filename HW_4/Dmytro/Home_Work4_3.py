number = int(input('Enter number: '))
n1 = 0
n2 = 1
for i in range(1, number + 1):

    print(n1)
    n1, n2 = n2,  n1 + n2
