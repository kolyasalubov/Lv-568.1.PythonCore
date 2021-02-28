# ######## Изменение типа данных #############
# int_lst = [i for i in range(int(input()))]
# float_lst = [float(x) for x in int_lst]
# print(float_lst)
# ##########
# int_lst = []
# x = int(input("Вводи значение листа x=",))
# int_lst.append(x)
# float_lst = [float(x) for x in int_lst]
# print(float_lst)

# ################
# a = []
# i = 0
# while i < 5:
#     x = int(input("Введи целое число списка: "))
#     a.append(x)
#     print(a)
#     i += 1
# print("Целочисленный список", a)
# b = [float(x) for x in a]
# print("Список с плавающим знаком", b)


list_len = int(input("Enter the len of list: "))
int_list = []

for x in range(list_len):
    y = int(input("Enter number: "))
    int_list.append(y)
print("Integer elements:", int_list)

for i in range(list_len):
    int_list[i] = float(int_list[i])
print("Float elements:", int_list)
