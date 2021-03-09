def zero_fuel(distance_to_pump, mpg, fuel_left):
    result = int((mpg * fuel_left)/distance_to_pump )
    return(bool(result))