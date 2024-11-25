import pygame

class afficherCouleurs():

    @staticmethod
    def afficher(screen):
        pionJaune = pygame.image.load('ressources/img/jaune.png')
        pionJaune = pygame.transform.scale(pionJaune,(50,70))
        pionNoir = pygame.image.load('ressources/img/noir.png')
        pionNoir = pygame.transform.scale(pionNoir,(60,80))
        pionBleu = pygame.image.load('ressources/img/bleu.png')
        pionBleu = pygame.transform.scale(pionBleu,(50,70))
        pionOrange = pygame.image.load('ressources/img/orange.png')
        pionOrange = pygame.transform.scale(pionOrange,(50,70))
        pionRose = pygame.image.load('ressources/img/rose.png')
        pionRose = pygame.transform.scale(pionRose,(60,65))
        pionRouge = pygame.image.load('ressources/img/rouge.png')
        pionRouge = pygame.transform.scale(pionRouge,(50,70))

        screen.blit(pionRouge, (650, 70))
        screen.blit(pionRose, (700, 150))
        screen.blit(pionOrange, (650, 230))
        screen.blit(pionBleu, (705, 310))
        screen.blit(pionNoir, (650, 380))
        screen.blit(pionJaune, (705, 480))