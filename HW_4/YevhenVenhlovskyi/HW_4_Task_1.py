# Calculation of x factorial
y=1
x=int(input('Enter integer number to calculate the factorial of it: '))
for x in range(1,x+1):
    y*=x
print('x factorial equals:', y)