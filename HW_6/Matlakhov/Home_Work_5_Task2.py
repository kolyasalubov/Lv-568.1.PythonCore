my_log = str(input("Введи логин: "))

while my_log != "First":
    print("Логин не верен. Введи еще раз: ")
    my_log = str(input("Введи логин: "))
print(f"Приветствую  {my_log}")
