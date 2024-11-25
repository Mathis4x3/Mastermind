from src.object.Niveaux.Niveau1 import Niveau1
from src.object.Niveaux.NiveauGen import NiveauGen


class Niveau(NiveauGen):

    niveauActuel = None

    @staticmethod
    def getNiveau():
        if Niveau.niveauActuel is None:
            return None
        return Niveau.niveauActuel.getNiveau()

    @staticmethod
    def getTentative():
        return Niveau.niveauActuel.getNiveau()

    @staticmethod
    def estDoubleCouleur():
        return Niveau.niveauActuel.estDoubleCouleur

    @staticmethod
    def setNiveauActuel(nouveauNiveau):
        Niveau.niveauActuel = nouveauNiveau