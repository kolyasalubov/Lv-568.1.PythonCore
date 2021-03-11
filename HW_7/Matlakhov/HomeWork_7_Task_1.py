import HW_7_Task_1_result
print('Выбери фигуру площадь которой нужно вычислить ')
num = int(
    input('Если прямоугольник введи:1, если триугольник введи:2, если круг:3 = '))

if num == 1:
    a = float(input('Введи сторону четырехугольника: '))
    b = float(input('Введи вторую сторону: '))
    print(HW_7_Task_1_result.rectangle(a, b))

elif num == 2:
    a = float(input('Введи основание трехугольника: '))
    h = float(input('Введи высоту трехугольника: '))
    print(HW_7_Task_1_result.triangle(h, a))

elif num == 3:
    r = float(input('Введи радиус круга: '))
    print(HW_7_Task_1_result.circle(r))
else:
    print('Вы ввели не верное значение')
    num = int(
        input('Если прямоугольник введи:1, если триугольник введи:2, если круг:3 = '))
