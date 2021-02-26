class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)  #super().__init__(3) 
    
    def findArea(self):
        a, b = self.sides
        area = a*b
        print('The area of the rectangle is ' + str(area))

#t = Polygon(3)

t = Rectangle()

t.inputSides()
# Enter side 1 : 3
# Enter side 2 : 5
# Enter side 3 : 4

#t.dispSides()
# Side 1 is 3.0
# Side 2 is 5.0
# Side 3 is 4.0

t.findArea()
# The area of the triangle is 6.00
