import pygame
from pygame.locals import *
from pathlib import Path
from labyrinth.Labyrinth import Labyrinth, Wall
from labyrinth.Player import Player
from labyrinth.Text_Display import Text

class App:
    """class for the labyrinth game"""

    windowWidth = 650
    windowHeight = 650
    player = 0

    def __init__(self):
        """initialize the application"""

        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.labyrinth = Labyrinth()
        self.player = Player()
        self.clock = pygame.time.Clock()
        self.text = Text(self.windowWidth, self.windowHeight)
        self.win = False

    def on_init(self):
        """initialize pygame, set display, and initialize the surfaces for use"""

        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('The Labyrinth')
        self._running = True
        self._image_surf = pygame.transform.scale(pygame.image.load(str(Path(__file__).parent / "sprites/panda_player.png")).convert(),
                                                 (self.labyrinth.pixelsize,self.labyrinth.pixelsize))
        self._block_surf = pygame.transform.scale(pygame.image.load(str(Path(__file__).parent / "sprites/wall.png")).convert(),
                                                 (self.labyrinth.pixelsize,self.labyrinth.pixelsize))
        self._end_rect_surf = pygame.transform.scale(pygame.image.load(str(Path(__file__).parent / "sprites/end_rect.png")).convert(),
                                                    (self.labyrinth.pixelsize,self.labyrinth.pixelsize))


    def on_event(self, event):
        """check the events"""
        if event.type == QUIT:
            self._running = False

    def on_win(self):
        """display the win screen and ask to continue"""
        self._display_surf.fill((0,0,0))
        self.text.display_text(self._display_surf, "You Won!", 115)
        self.text.display_text(self._display_surf, "Would you like to keep playing? y or n", 40, self.windowWidth / 2, self.windowHeight / 1.25)

    def on_loop(self):
        """checks for collisions with labyrinth rects"""
        for wall in self.labyrinth.wall_list:
            if self.player.rect.colliderect(self.labyrinth.end_rect):
                self.win = True

            if self.player.rect.colliderect(wall.rect):

                #player hits the left side of the wall
                if self.player.rect.x > wall.rect.x:
                    self.player.rect.x += self.player.speed

                #player hits the right side of the wall
                if self.player.rect.x < wall.rect.x:
                    self.player.rect.x -= self.player.speed

                #player hits the top of the wall
                if self.player.rect.y > wall.rect.y:
                    self.player.rect.y += self.player.speed

                #player hits the bottom of the wall
                if self.player.rect.y < wall.rect.y:
                    self.player.rect.y -= self.player.speed

    def on_render(self):
        """render the images of the labyrinth onto the screen"""
        if self.win is True:
            self.on_win()
        else:
            self._display_surf.fill((0,0,0))
            self._display_surf.blit(self._image_surf, (self.player.rect.x, self.player.rect.y))
            self.labyrinth.draw(self._display_surf, self._block_surf, self._end_rect_surf)
        pygame.display.flip()

    def on_cleanup(self):
        """exit the game"""
        pygame.quit()

    def on_execute(self):
        """main loop for the application, deals with player input"""
        if self.on_init() is False:
            self._running = False

        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                self.player.moveRight()

            elif keys[K_LEFT]:
                self.player.moveLeft()

            elif keys[K_UP]:
                self.player.moveUp()

            elif keys[K_DOWN]:
                self.player.moveDown()

            elif keys[K_ESCAPE]:
                self._running = False

            elif keys[K_y] and self.win is True:
                self.win = False
                self.labyrinth = Labyrinth()
                self.player = Player()

            elif keys[K_n] and self.win is True:
                self._running = False


            self.on_loop()
            self.on_render()

            self.clock.tick(120)

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
