from src.controleur.ControleurCode import ControleurCode
from src.object.Niveaux.Niveau import Niveau
from src.object.Niveaux.Niveau1 import Niveau1
from src.object.Niveaux.Niveau2 import Niveau2
from src.object.data.Couleur import Couleur

Niveau.setNiveauActuel(Niveau1())
code = ControleurCode.genererCodeAleatoire()
code.toString()