import pygame
import constants
"""constats include just some variables like screen size colors or fps toggle"""


class SpriteSheet(object):
    def __init__(self, file_name):
        """loading spritesheet image"""
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height,colorkey =constants.WHITE):
        image = pygame.Surface([width, height]).convert()
        """part of sheet on image surface"""
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        """set color key"""
        image.set_colorkey(colorkey)
        return image


