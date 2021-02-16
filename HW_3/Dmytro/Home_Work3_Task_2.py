a = int(input('Enter a:'))
b = [0, 0, 0, 0]

b[0] = a % 10

a = int(a/10)
b[1] = a % 10

a = int(a/10)
b[2] = a % 10

a = int(a/10)
b[3] = a % 10

print(b[0]*b[1]*b[2]*b[3])
print(b)
print(sorted(b))
