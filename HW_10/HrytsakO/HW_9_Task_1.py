try:
    age = int(input(": "))
    def even_or_odd(age):
        if age % 2 == 0 and age >= 0:
            return "Your age is even"
        elif age % 2 == 1 and age >= 0:
            return "Your age is odd"
        else:
            print("Error")
    print(even_or_odd(age))
    
except ValueError:
    print("ValueError")

