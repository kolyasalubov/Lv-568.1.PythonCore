def zero_fuel(distance_to_pump, mpg, fuel_left):
    """function name zero_fuel
        input parametrs thrie: distance_to_pump, mpg, fuel_left
        return comparison result
    """
    return distance_to_pump <= mpg *  # fuel_left сравниваем дист. и ост. топ. результат в bool форме


d = int(input("distance_to_pump"))
b = int(input("mpg"))
c = int(input("fuel_left"))
n = zero_fuel(d, b, c)
print(n)
