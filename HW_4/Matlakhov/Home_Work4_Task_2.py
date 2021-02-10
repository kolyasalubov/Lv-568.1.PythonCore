######## Изменение типа данных #############
int_lst = [i for i in range(int(input()))]
float_lst = [float(x) for x in int_lst]
print(float_lst)
##########
int_lst = []
x = int(input("Вводи значение листа x=",))
int_lst.append(x)
float_lst = [float(x) for x in int_lst]
print(float_lst)

################
a = []
i = 0
while i < 5:
    x = int(input("Введи целое число списка: "))
    a.append(x)
    print(a)
    i += 1
print("Целочисленный список", a)
b = [float(x) for x in a]
print("Список с плавающим знаком", b)
