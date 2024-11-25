from src.object.Niveaux.NiveauGen import NiveauGen


class Niveau2(NiveauGen):

    @staticmethod
    def estDoubleCouleur():
        return False

    @staticmethod
    def getTentative():
        return 8

    @staticmethod
    def getNiveau():
        return 2