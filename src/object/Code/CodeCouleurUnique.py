import random
from types import CodeType

from src.object.Code.Code import Code
from src.object.Code.GenererCode import GenererCode


class CodeCouleurUnique(GenererCode):
    def generer(self):
        code = Code()
        nb = 0
        while nb != 4:
            couleur = random.choice(self.couleurs)
            if not code.contient(couleur) :
                code.ajouterCouleur(couleur)
                nb += 1

        return code