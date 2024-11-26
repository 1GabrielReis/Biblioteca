from abc import ABC, abstractmethod
from typing import List

from ..entities.reserva import Reserva

class ReservaDao(ABC):
    @abstractmethod
    def insert(self,reserva: Reserva):
        pass

    @abstractmethod
    def update(self,reserva: Reserva):
        pass

    @abstractmethod
    def deleteById(self,id: int):
        pass

    @abstractmethod
    def findById(self,id: int):
        pass

    @abstractmethod
    def findAll(self,reserva: List[Reserva]):
        pass
