import pygame


class Screen:
    instance = None
    width = 1000
    height = 700

    @staticmethod
    def getScreen():
        if Screen.instance is None:
            Screen.instance = pygame.display.set_mode((Screen.width, Screen.height))
        return Screen.instance

    @staticmethod
    def setScreen(screen):
        Screen.instance = screen