class Polygon:
    def __init__(self, *args):
        self.args = args
    
    def square(self):
        pass

class Rectangle(Polygon):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a*self.b