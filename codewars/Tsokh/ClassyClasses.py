class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"
    
    def getInfo(self):
        i = 0
        self.info = f"{self.name[i]}s age is {self.age[i]}"
        i += 1
        return self.info
        