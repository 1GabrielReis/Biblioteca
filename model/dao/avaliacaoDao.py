from abc import ABC, abstractmethod
from typing import List

from ..entities.avaliacao import Avaliacao
from ..entities.aluno import Aluno
from ..entities.livro import Livro
from ..entities.reserva import Reserva

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
    def findAll(self) -> List[Avaliacao]:
        pass

    @abstractmethod
    def findByAluno(self, avaliacao) -> List[Avaliacao]:
        pass

    @abstractmethod
    def findByLivro(self, avaliacao) -> List[Avaliacao]:
        pass

    @abstractmethod
    def findByReserva(self, avaliacao) -> List[Avaliacao]:
        pass
