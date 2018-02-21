import pygame
from pygame.locals import *
from Labyrinth import Labyrinth, Wall
from Player import Player

class App:

    windowWidth = 500
    windowHeight = 500
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.labyrinth = Labyrinth()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('The Labyrinth')
        self._running = True
        self._image_surf = pygame.transform.scale(pygame.image.load("panda_player.png").convert(), (50,50))
        self._block_surf = pygame.transform.scale(pygame.image.load("wall.png").convert(), (50,50))

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        for wall in self.labyrinth.wall_list:
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
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf, (self.player.rect.x, self.player.rect.y))
        self.labyrinth.draw(self._display_surf, self._block_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
