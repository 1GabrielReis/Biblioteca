from abc import ABC, abstractmethod
from typing import List

from ..entities.livro import Livro

class LivroDao(ABC):
    @abstractmethod
    def insert(self,livro: Livro):
        pass

    @abstractmethod
    def update(self,livro: Livro):
        pass

    @abstractmethod
    def deleteById(self,id: int):
        pass

    @abstractmethod
    def findById(self,id: int):
        pass

    @abstractmethod
    def findAll(self,livro) -> List[Livro]:
        pass