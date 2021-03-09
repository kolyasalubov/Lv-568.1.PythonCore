class Polygon:
    def __init__(self, no_of_sides):
        self.n=no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}:"))
                                                for i in range(self.n)]
    
class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
    def findArea(self):
        side_1,side_2=self.sides
        area = side_1*side_2
        return area

        
r=Rectangle()
r.inputSides()
print(f"The area of the rectangle is {r.findArea()}")
