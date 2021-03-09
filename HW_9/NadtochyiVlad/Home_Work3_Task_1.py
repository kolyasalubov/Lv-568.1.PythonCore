class Polygone():
    """Creating new Class Square of polygone"""
    def __init__(self,side_one,side_two):
        self.side_one = side_one
        self.side_two = side_two

    def rectangle_square(self):
        """Calculating square rectangle"""
        return self.side_one*self.side_two

class Rectangle(Polygone):
    """Creating new Class Square of Rectangle"""
    def __init__(self, side_one, side_two):
        super().__init__(side_one, side_two)



r_1 = Rectangle(2,9)

print(r_1.rectangle_square())