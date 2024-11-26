from abc import ABC, abstractmethod
from typing import List

from ..entities.avaliacao import Avaliacao

class ReservaDao(ABC):
    @abstractmethod
    def insert(self,avaliacao: Avaliacao):
        pass

    @abstractmethod
    def update(self,avaliacao: Avaliacao):
        pass

    @abstractmethod
    def deleteById(self,id: int):
        pass

    @abstractmethod
    def findById(self,id: int):
        pass

    @abstractmethod
    def findAll(self,avaliacao: List[Avaliacao]):
        pass
