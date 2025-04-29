from abc import ABC, abstractmethod

class Response_base(ABC):

    @abstractmethod
    def build_list(self, lista):
        pass

    @abstractmethod
    def build_detail(self, obj):
        pass

    @abstractmethod
    def serialize(self, obj):
        pass