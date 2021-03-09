class Polygon:
    """creating new class knows as Polygon"""
    def init(self, sides):
        self.sides = sides

    def get_perimeter(self):
        '''Calculating perimeter'''
        perimeter = sum(self.sides)
        return perimeter

class Rectangle(Polygon):
    """new Object known as Rectangle"""
    def __init__(self, sides):
        Polygon.init(self, sides)


t1 = Rectangle([4, 4, 6, 6])
perimeter = t1.get_perimeter()
print(perimeter)
