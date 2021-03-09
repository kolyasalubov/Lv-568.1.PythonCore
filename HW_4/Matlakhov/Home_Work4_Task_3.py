############# Фибоначчи  ######################

f = []
i = 0
x = 0
while i < n:

f1 = 1
f2 = 1

n = int(input("Номер элемента ряда Фибоначчи: "))

i = 0
while i < n - 2:
    f_sum = f1 + f2
    # print(f_sum)
    f1 = f2
   # print(f1)
   # print(f2)
    f2 = f_sum
   # print(f_sum)
    i = i + 1
print(f2)

##################

n1 = 0
n2 = 1
n3 = 0
x = int(input("Введи число элементов Фибоначчи: "))
for i in range(0, x):
    n3 = n1 + n3
    print(n3)
    n1 = n2
    n2 = n3
