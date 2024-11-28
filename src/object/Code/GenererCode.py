from abc import abstractmethod

from src.object.data.Couleur import Couleur


class GenererCode:
    couleurs = [Couleur.ROUGE, Couleur.ROSE, Couleur.BLEU, Couleur.JAUNE, Couleur.NOIR, Couleur.ORANGE]

    @abstractmethod
    def generer(self):
        ...