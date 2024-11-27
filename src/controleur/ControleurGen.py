from src.object.Screen import Screen
from src.vue.AfficherCouleurs import AfficherCouleurs
from src.vue.AfficherErreur import AfficherErreur


class ControleurGen:

    @staticmethod
    def afficherCouleurs():
        screen = Screen().getScreen()
        AfficherCouleurs().afficher(screen)

    @staticmethod
    def afficherErreur():
        screen = Screen().getScreen()
        AfficherErreur().error(screen)
        Screen.setScreen(screen)