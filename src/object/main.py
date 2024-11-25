from src.object.Niveaux.Niveau import Niveau
from src.object.Niveaux.Niveau1 import Niveau1
from src.object.Niveaux.Niveau2 import Niveau2

Niveau.setNiveauActuel(Niveau1())
print(Niveau.getNiveau())
Niveau.setNiveauActuel(Niveau2())
print(Niveau.getNiveau())