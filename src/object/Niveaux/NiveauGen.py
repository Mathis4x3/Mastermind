from abc import ABC, abstractmethod

class NiveauGen(ABC):

    @staticmethod
    @abstractmethod
    def getTentative():
        ...

    @staticmethod
    @abstractmethod
    def estDoubleCouleur():
        ...

    @staticmethod
    @abstractmethod
    def getNiveau():
        ...

