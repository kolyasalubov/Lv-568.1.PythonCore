import math

def distance(x1, y1, x2, y2):
    distance = round(math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)),2)
    return distance

