def distance(x1, y1, x2, y2):
    import math # Import math Library
    print (round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2))
distance(1, 1, 0, 0)

############################################
## without math library

# def distance(x1, y1, x2, y2):
#     print (round(((x2-x1)**2+(y2-y1)**2)**0.5), 2)
# distance(1, 1, 0, 0)