from abc import ABC, abstractmethod

class Controller_base(ABC):

    @abstractmethod
    def insert(self, service):
        pass

    @abstractmethod
    def update(self, service):
        pass

    @abstractmethod
    def deleteById(self,id: int):
        pass

    @abstractmethod
    def findById(self,id: int):
        pass

    @abstractmethod
    def findAll(self):
        pass
    