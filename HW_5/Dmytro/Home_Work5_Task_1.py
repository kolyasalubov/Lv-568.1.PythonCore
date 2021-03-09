print("even num:")
x=[]
for x in range(10):
    if x % 2 == 0:
        print (x)

print("odd num:")
for x in range(10):
    if x % 2 == 1:
        print (x)

print("num is not divisible by two and three:")
for x in range(10):
    if x % 2 == 1 and x % 3 == 1:
        print (x)
