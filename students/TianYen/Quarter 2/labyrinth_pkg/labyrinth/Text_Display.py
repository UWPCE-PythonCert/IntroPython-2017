import pygame

class Text:

    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height

    def text_object(self, text, font):
        """function that takes text and a font as input and returns a surface object and its given rectangle"""
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()

    def display_text(self, display_surf, text, size, x=0, y=0):
        """display the text to the given surface, can customize the size, and location of text.  default for location is the center"""
        largeText = pygame.font.SysFont('freesansbold.ttf', size)
        textSurface, textRect = self.text_object(text, largeText)
        if x == 0  and y == 0:
            textRect.center = (int(self.display_width / 2), int(self.display_height / 2))
        else:
            textRect.center = (int(x), int(y))
        display_surf.blit(textSurface, textRect)
