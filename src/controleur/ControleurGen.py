from src.object.Screen import Screen
from src.vue.afficherCouleurs import afficherCouleurs


class ControleurGen:

    @staticmethod
    def afficherCouleurs():
        screen = Screen().getScreen()
        afficherCouleurs().afficher(screen)