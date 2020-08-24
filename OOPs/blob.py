import random
class Blob:
    # giving more control to the user hands without enforcing the predefined restrictions
    # we let the user give the ability to select whethet they want to change the measurements such as movemement speed
    # border of till where the blods will move  around
    # This will help us to  user to work with their code more sofistically rather than looking for the blob class and changing it
#known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class

    def __init__(self, color, x_border,y_border,size_range=(4,8),movement_range=(-1,2)):
       self.size=random.randrange(size_range[0],size_range[1])
       self.x_border=x_border
       self.y_border=y_border
       self.x = random.randrange(0, x_border)
       self.y = random.randrange(0, y_border)
       self.movement_range=movement_range
       self.color = color
#other  methods that helps us to move shape
    def move(self):
        self.move_x = random.randrange(self.movement_range[0], self.movement_range[1])
        self.move_y = random.randrange(self.movement_range[0], self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_border:
            self.x = self.x_border

        if self.y < 0:
            self.y = 0
        elif self.y > self.y_border:
            self.y = self.y_border
