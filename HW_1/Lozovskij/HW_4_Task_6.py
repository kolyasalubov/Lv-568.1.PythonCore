nterm = int(input("enter your number? : "))

n1, n2 = 0, 1

while n1 < nterm:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    