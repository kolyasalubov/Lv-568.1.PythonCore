class Polygon:

    def init(self, side):
        self.side = side

    def get_perimeter(self):
        '''Calculating perimeter'''
        perimeter = sum(self.side)
        return perimeter


class Rectangle(Polygon):

    def __init__(self, side):
        Polygon.init(self, side)


t1 = Rectangle([4, 4, 6, 6])
perimeter = t1.get_perimeter()
print(perimeter)
