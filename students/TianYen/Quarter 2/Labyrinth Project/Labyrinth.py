import pygame
from random import choice, randrange

class Labyrinth:
    """class that creates a Labyrinth object"""

    def __init__(self, row=25, col=25):
        self.row = row
        self.col = col
        self.labyrinth = self.get_labyrinth(row, col)
        self.wall_list = self.get_walls(self.labyrinth, row, col)


    @staticmethod
    def get_labyrinth(row, col):
        """return a random matrix of size row by column"""

        #create a random labyrinth
        lab = [[choice([0,1]) for x in range(col)] for i in range(row)]

        #add some conditions to the labyrinth
        end_rect = pygame.Rect(randrange(1, row) * 50, randrange(1, col) * 50, 50, 50)
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 2:
                    lab[i][j] = 1
                    lab[i][-1] = 1

                if j == 0 or j == col - 2:
                    lab[i][j] = 1
                    lab[i][-1] = 1

                if i == (end_rect.x / 50) and j ==  (end_rect.y / 50):
                    lab[i][j] = end_rect
        #lab = [[choice([0,1]) for x in range(col)] for i in range(row)]
        return lab

    @staticmethod
    def get_walls(labyrinth, row, col):
        walls = []
        for i in range(row):
            for j in range(col):
                if labyrinth[i][j] == 1:
                    walls.append(Wall(j * 50, i * 50))
        return walls

    def draw(self, display_surf, image_surf):
        for i in range(self.row):
            for j in range(self.col):
                if self.labyrinth[i][j] == 1:
                    display_surf.blit(image_surf, (j * 50, i * 50))


class Wall():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 50, 50)
