from abc import ABC, abstractmethod
from typing import List

from ..entities.aluno import Aluno

class AlunoDao(ABC):
    @abstractmethod
    def insert(self,aluno: Aluno):
        pass

    @abstractmethod
    def update(self,aluno: Aluno):
        pass

    @abstractmethod
    def deleteById(self,id: int):
        pass

    @abstractmethod
    def findById(self,id: int):
        pass

    @abstractmethod
    def findAll(self,aluno: List[Aluno]):
        pass
