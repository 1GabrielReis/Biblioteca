from abc import ABC, abstractmethod
from typing import List

from ..entities.reserva import Reserva
from ..entities.livro import Livro
from ..entities.aluno import Aluno

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
    def findAll(self) -> List[Reserva]:
        pass

    @abstractmethod
    def findByLivro(self, livro: Livro) -> List[Livro]:
        pass

    @abstractmethod
    def findByAluno(self, aluno: Aluno) -> List[Aluno]:
        pass

    @abstractmethod
    def returnBook(self, reserva: Reserva):
        pass