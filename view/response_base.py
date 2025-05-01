from abc import ABC, abstractmethod

class Response_base(ABC):

    @abstractmethod
    def format(data):
        pass

    @abstractmethod
    def format_list(data):
        pass