from src.object.data.Couleur import Couleur


class Code:
    def __init__(self):
        self.taille = 0
        self.couleurs = []

    def cloner(self):
        new = Code()
        for couleur in self.couleurs:
            new.ajouterCouleur(couleur)
        return new

    def getTaille(self):
        return self.taille

    def ajouterCouleur(self, couleur):
        if self.taille != 4:
            self.couleurs.append(couleur)
            self.taille += 1
            return True
        return False

    def remplacerParNull(self, indice):
        self.couleurs[indice] = None

    def enleverDerniereCouleur(self):
        if len(self.couleurs) != 0:
            self.couleurs.pop(self.taille -1)
            self.taille -= 1
            return True
        return False

    def contient(self, couleur):
        return couleur in self.couleurs

    def nbCouleurDansCode(self, couleur):
        compt = 0
        for i in range(len(self.couleurs)):
            if self.couleurs[i].name == couleur.name:
                compt += 1
        return compt

    def toString(self):
        for couleur in self.couleurs:
            print(couleur.name)

    def vider(self):
        self.couleurs = []
        self.taille = 0

    def getCouleur(self, indice):
        return self.couleurs[indice]