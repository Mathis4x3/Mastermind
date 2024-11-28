import random

from src.object.Code.Code import Code
from src.object.Code.GenererCode import GenererCode


class CodeCouleurDouble(GenererCode):
    def generer(self):
        nb = 0
        code = Code()
        while nb != 4:
            couleur = random.choice(self.couleurs)
            if code.nbCouleurDansCode(couleur) < 2:
                code.ajouterCouleur(couleur)
                nb += 1
        return code

