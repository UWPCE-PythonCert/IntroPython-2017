import pygame

class Player:
    """class that creates a player object with simple movement abilities"""
    speed = 2

    def __init__(self):
        self.rect = pygame.Rect(50, 50, 50,50)

    def moveRight(self):
        """moves the player to the right a distance of the variable speed"""
        self.rect.move_ip(self.speed, 0)

    def moveLeft(self):
        """moves the player to the left a distance of the variable speed"""
        self.rect.move_ip(-self.speed, 0)

    def moveUp(self):
        """moves the player up a distance of the variable speed"""
        self.rect.move_ip(0, -self.speed)

    def moveDown(self):
        """moves the player down a distance of the variable speed"""
        self.rect.move_ip(0, self.speed)
