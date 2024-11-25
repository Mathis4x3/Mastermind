import pygame


class Screen:
    instance = None
    width = 1000
    height = 700

    @staticmethod
    def getScreen():
        if Screen.instance == None:
            Screen.instance = pygame.display.set_mode((Screen.width, Screen.height))
        return Screen.instance

