import pygame
from random import choice, randrange


class Labyrinth:
    """class that creates a Labyrinth object"""
    pixelsize = 25

    def __init__(self, row=25, col=25):
        """initialize the Labyrinth class"""
        self.row = row
        self.col = col
        self.wl = []
        self.end_rect = pygame.Rect(self.get_random_location(row) * self.pixelsize, self.get_random_location(col) * self.pixelsize, self.pixelsize, self.pixelsize)
        self.labyrinth = self.get_borders()
        #better way here?
        self.maze_generator(int(self.end_rect.x / self.pixelsize), int(self.end_rect.y / self.pixelsize))
        self.wall_list = self.get_walls(self.labyrinth, row, col, self.pixelsize, self.end_rect)

    @staticmethod
    def get_random_location(k):
        """take a number k and return a random value from 1 to k - 1, always odd"""
        return randrange(1, k - 1, 2)

    @staticmethod
    def get_walls(labyrinth, row, col, pixelsize, end_rect):
        """static method that iterates over the labyrinth and initializes the wall objects"""
        walls = []
        for i in range(row):
            for j in range(col):
                if labyrinth[i][j] in (1,2):
                    walls.append(Wall(j * pixelsize, i * pixelsize))
        return walls

    def get_borders(self):
        """create the borders for the matrix setting all values to 2"""

        maze = [[1 for x in range(self.col)] for i in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):

                if i in (0, self.row - 1) or j in (0, self.col - 1):
                    maze[i][j] = 2

        return maze

    def peek(self, wall):
        """function that checks if there are walls surrounding the current cell"""
        #check four directions to see if we have visited any cells
        try:
                #east
            if wall.direction == 'east':
                if self.labyrinth[wall.x + 1][wall.y] == 1:
                    return True
                #west
            elif wall.direction == 'west':
                if self.labyrinth[wall.x - 1][wall.y] == 1:
                    return True
                #north
            elif wall.direction == 'north':
                if self.labyrinth[wall.x][wall.y + 1] == 1:
                    return True
                #south
            elif wall.direction == 'south':
                if self.labyrinth[wall.x][wall.y - 1] == 1:
                    return True

            else:
                return False
        except IndexError:
            pass

    def check_direction(self, func, wall):
        """take a function and a wall as input, checks which direction the wall is and returns the function for that direction"""
        #east
        if wall.direction == 'east':
            return func(wall.x + 1, wall.y)
        #west
        if wall.direction == 'west':
            return func(wall.x - 1, wall.y)
        #north
        if wall.direction == 'north':
            return func(wall.x, wall.y + 1)
        #south
        if wall.direction == 'south':
            return func(wall.x, wall.y - 1)

    def maze_generator(self, x, y):
        """generates the maze starting from the first x,y input according to prim's maze algorithm"""
        self.labyrinth[x][y] = 0

            #add the four surrounding cells to the wall list
        self.wl.append(Wall(x + 1, y, 'east'))
        self.wl.append(Wall(x - 1, y, 'west'))
        self.wl.append(Wall(x, y + 1, 'north'))
        self.wl.append(Wall(x, y - 1, 'south'))

        while len(self.wl) > 0:
            rand_wall = choice(self.wl)
            if self.peek(rand_wall):
                self.labyrinth[rand_wall.x][rand_wall.y] = 0
                self.check_direction(self.maze_generator, rand_wall)
            else:
                self.wl.remove(rand_wall)

    def draw(self, display_surf, image_surf, end_rect_surf):
        """iterates over the labyrinth matrix and blits the images onto the gui"""
        for i in range(self.row):
            for j in range(self.col):
                if self.labyrinth[i][j] == 1 or self.labyrinth[i][j] == 2:
                    display_surf.blit(image_surf, (j * self.pixelsize, i * self.pixelsize))
                if i == int(self.end_rect.y / self.pixelsize) and j == int(self.end_rect.x / self.pixelsize):
                    display_surf.blit(end_rect_surf, (j * self.pixelsize, i * self.pixelsize))


class Wall():
    """class that is the base for all the walls of the labyrinth"""
    pixelsize = 25

    def __init__(self, x, y, direction=None):
        """initialize the wall object, with x,y coordinates and optional cardinal direction (north,south,east,west)"""
        self.direction = direction
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.pixelsize, self.pixelsize)
