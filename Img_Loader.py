import os
import pygame
import constants


def load_img(filename, size, path="data/img"):
    img = pygame.image.load(os.path.join(path, filename))
    img = pygame.transform.scale(img, size)
    img = img.convert()
    img.set_colorkey(constants.BLACK)
    return img


def rotate_img(img, angle):
    img = img
    img = pygame.transform.rotate(img, angle)
    img.convert()
    return img