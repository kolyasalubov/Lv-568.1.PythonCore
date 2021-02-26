## Color Ghost

import random

class Ghost(object):
    colors = ["white", "yellow", "purple", "red"]
    
    def __init__(self):
        self.color = random.choice(Ghost.colors)
        print(self.color)

Ghost ()

# import random

# class Ghost (object):
#   def __init__(self):
#     self.color = random.choice(["white", "yellow", "purple", "red"])
#     print(self.color)

# Ghost ()