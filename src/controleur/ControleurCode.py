from src.object.Niveaux.Niveau import Niveau


class ControleurCode:

    @staticmethod
    def genererCodeAleatoire():
        return Niveau.getTypeGenererCode().generer()