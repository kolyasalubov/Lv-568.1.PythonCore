nterm = int(input("How many terms? : "))
n1, n2 = 0, 1
count = 0

while n1 < nterm:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1