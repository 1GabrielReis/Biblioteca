from abc import ABC, abstractmethod
from typing import List

from ..entities.biblioteca import Biblioteca
from ..entities.aluno import Aluno

class BibliotecaDao(ABC):

    @abstractmethod
    def insert(self,biblioteca: Biblioteca):
        pass

    @abstractmethod
    def update(self,biblioteca: Biblioteca):
        pass

    @abstractmethod
    def deleteById(self,id: int):
        pass

    @abstractmethod
    def findById(self,id: int):
        pass

    @abstractmethod
    def findAll(self,biblioteca: List[Biblioteca]):
        pass

    @abstractmethod
    def findByAluno(self, aluno: Aluno) -> List[Aluno]:
        pass
