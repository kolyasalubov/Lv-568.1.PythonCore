length = int(input("How many circles? "))
n1 = 0
n2 = 1
itteration = 0
if length<0:
    print("enter correct number")
else:
    while itteration < length:
        print(n1)
        nn = n1 + n2
        n1 = n2
        n2 = nn
        itteration += 1
       
