import pygame
from Balloon import Balloon

class Fish(Balloon):

    def __init__ (self, screen, settings):

        Balloon.__init__(self, screen, settings)
        self.image = pygame.image.load('resources/fishh.png')