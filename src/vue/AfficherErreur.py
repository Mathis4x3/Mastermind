import time
from turtledemo.nim import COLOR

import pygame
from pygame import BLEND_RGBA_MULT, Color


class AfficherErreur:

    warning = pygame.image.load('ressources/img/warning.png')

    @staticmethod
    def error(screen):
        AfficherErreur.warning = pygame.transform.scale(AfficherErreur.warning, (100, 100))
        screen.blit(AfficherErreur.warning, (450, 250))
        pygame.display.flip()
        time.sleep(1 / 4)
        pygame.draw.rect(screen, (255,255,255),(450,250,100,100))
        pygame.display.flip()