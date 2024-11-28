from src.object.Code.CodeCouleurDouble import CodeCouleurDouble
from src.object.Niveaux.NiveauGen import NiveauGen


class Niveau3(NiveauGen):

    @staticmethod
    def getTypeGenererCode():
        return CodeCouleurDouble()

    @staticmethod
    def estDoubleCouleur():
        return True

    @staticmethod
    def getTentative():
        return 8

    @staticmethod
    def getNiveau():
        return 3