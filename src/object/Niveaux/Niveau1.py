from src.object.Code.CodeCouleurUnique import CodeCouleurUnique
from src.object.Niveaux.NiveauGen import NiveauGen


class Niveau1(NiveauGen):

    @staticmethod
    def getTypeGenererCode():
        return CodeCouleurUnique()

    @staticmethod
    def estDoubleCouleur():
        return False

    @staticmethod
    def getTentative():
        return 10

    @staticmethod
    def getNiveau():
        return 1