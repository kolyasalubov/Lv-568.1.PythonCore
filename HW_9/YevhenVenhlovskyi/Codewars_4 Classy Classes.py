## Classy Classes

class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"
        print(self.info)

# Test.describe("Basic tests")
names=["john","matt","alex","cam"]
ages=[16,25,57,39]
for i in range(4):
    name,age=names[i],ages[i]
    person=Person(name,age)
    # Test.it("Testing for %s and %s" %(repr(name),age))
    # Test.assert_equals(person.info, name+"s age is "+str(age))


##################################################################
# class Person:
#     def __init__(self, name: str, age: int):
#         """ Prepare data. """
#         self.name = name
#         self.age = age
#     @property
#     def info(self):
#         """ Get person info. """
#         return f"{self.name}s age is {self.age}"