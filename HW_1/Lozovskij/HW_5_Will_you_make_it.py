def zero_fuel(distance_to_pump, mpg, fuel_left):
    result = int((mpg * fuel_left)/distance_to_pump)
    return(bool(result))
    
    #if distunce_to_pump / mpg <= fuel_left:
        #return True
    #else:
        #return False
        