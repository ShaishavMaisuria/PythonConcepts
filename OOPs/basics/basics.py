import pygame
import random
#this code used for reference purpose only and that I have learned all this concepts
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
STARTING_BLUE_BLOBS = 10 # creating the number of blue blobs
STARTING_RED_BLOBS = 3# creating the number of red blobs
class Blob:
#known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class

    def __init__(self, color, x_border,y_border):
        self.x_border=x_border
        self.y_border=y_border
        self.x = random.randrange(0, x_border)
        self.y = random.randrange(0, y_border)
        self.size = random.randrange(4, 8)
        self.color = color
#other  methods that helps us to move shape
    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0:
            self.x = 0
        elif self.x > self.x_border:
            self.x = self.x_border

        if self.y < 0:
            self.y = 0
        elif self.y > self.y_border:
            self.y = self.y_border


#sets the window size
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
#application name on the window
pygame.display.set_caption('Blob World')
#timer
clock = pygame.time.Clock()


#will help us to draw on the window
def draw_environment(blob_list):
    #paint all canvas of the window whit before starting
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob=blob_dict[blob_id]

            #creating the shape on the screen and giving the attritubutes of the shape
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            # moving the shape in short moving the object or changig the posiiont of the object
            blob.move()
#refressing each of the movements after drawimg
    pygame.display.update()

#The main function in Python acts as the point of execution for any program. Defining the main function in Python programming is a necessity to start the execution of the program as it gets executed only when the program is run directly and not executed when imported as a module  (edureka)
def main():
    #creating the enumerate is used as a iterator to keep track of th each and every object associated with id or  value of counter

    blue_blobs = dict(enumerate([Blob(BLUE,WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([Blob(RED,WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))


    #we keep  checking if the player has selected quit or not
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs,red_blobs])
        clock.tick(60)


if __name__ == '__main__':
    main()