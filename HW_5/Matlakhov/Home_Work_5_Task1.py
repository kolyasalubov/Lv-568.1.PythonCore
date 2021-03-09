x = int(input("Сколько эллементов будет: "))
l = []
i = 0
while i < x:
    a = int(input("Введи следующее число: "))
    l.append(a)
    i += 1
print(l)
a, d, c = [], [], []
i = 0
for i in l:
    if i % 2 == 0:
        a.append(i)
    else:
        if i % 3 == 0:
            d.append(i)
            i += 1
        else:
            c.append(i)

            i += 1
print("Числа которые делятся на 2", a)
print("Числа которые делятся на 3", d)
print("Числа которые не делятся на 2 и 3", c)
