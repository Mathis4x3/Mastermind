from src.object.Niveaux.NiveauGen import NiveauGen


class Niveau1(NiveauGen):

    @staticmethod
    def estDoubleCouleur():
        return False

    @staticmethod
    def getTentative():
        return 10

    @staticmethod
    def getNiveau():
        return 1