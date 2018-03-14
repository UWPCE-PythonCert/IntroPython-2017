import pygame

class Player:
    """class that creates a player object with simple movement abilities"""
    speed = 1
    pixelsize = 25

    def __init__(self, x=25, y=25):
        """initialize the player object with optional conditions of coordinates for initialization"""
        self.rect = pygame.Rect(x, y, self.pixelsize, self.pixelsize)


    def moveRight(self):
        """moves the player rectangle to the right a distance of the variable speed"""
        self.rect.move_ip(self.speed, 0)

    def moveLeft(self):
        """moves the player rectangle to the left a distance of the variable speed"""
        self.rect.move_ip(-self.speed, 0)

    def moveUp(self):
        """moves the player rectangle up a distance of the variable speed"""
        self.rect.move_ip(0, -self.speed)

    def moveDown(self):
        """moves the player rectangledown a distance of the variable speed"""
        self.rect.move_ip(0, self.speed)
