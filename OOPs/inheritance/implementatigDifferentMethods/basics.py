import pygame
import random
#this code used for reference purpose only and that I have learned all this concepts
from OOPs.blob import Blob

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
STARTING_BLUE_BLOBS = 10 # creating the number of blue blobs
STARTING_RED_BLOBS = 3# creating the number of red blobs
# The new BlueBlob class, inheriting from Blob is our "child" class, or "subclass." When inheriting from another class, you are inheriting everything, all of the methods, including the special methods. Thus, in this case, we're inheriting everything and changing nothing. We can, however, now add our own methods, or even overwrite methods.
# We've overwritten the original dunder init method! So do we need to basically write all of the code from the original init method? Nope! We have super() at our disposal!

class BlueBlob(Blob):
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        # can replace above line with line below main reason is that
        # we can also make sure that the class remains more easily accesible if changed
        # mainly keep it less static
        # Blob.__init__(self, color, x_boundary, y_boundary)
        self.color = BLUE

    #we can also modify other methods too
    def move_fast(self):
        self.x += random.randrange(-5, 5)
        self.y += random.randrange(-5, 5)


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
            #blob.move() changing it to line below
            blob.move_fast()
            blob.check_bounds()
#refressing each of the movements after drawimg
    pygame.display.update()

#The main function in Python acts as the point of execution for any program. Defining the main function in Python programming is a necessity to start the execution of the program as it gets executed only when the program is run directly and not executed when imported as a module  (edureka)
def main():
    #creating the enumerate is used as a iterator to keep track of th each and every object associated with id or  value of counter

    blue_blobs = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([BlueBlob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))

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