import pygame
from labyrinth.Text_Display import Text

windowWidth = 500
windowHeight = 500
surface = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE)



def test_text_initialize():
    text = Text(windowWidth / 2, windowHeight / 2)


def test_text_object():
    pygame.font.init()

    text = Text(windowWidth, windowHeight)
    textSurf, textRect = text.text_object("Hello", pygame.font.SysFont('freesansbold.ttf', 100))
    assert isinstance(textSurf, pygame.Surface)
    assert isinstance(textRect, pygame.Rect)


def test_text_display():
    windowWidth = 500
    windowHeight = 500
    surface = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE)

    text = Text(windowWidth, windowHeight)
    text.display_text(surface, "Hello", 100)
    text.display_text(surface, "Yes", 100, 50, 50)
