from ..controller_base import Controller_base
from ...models.service.alunoService import AlunoService
from ...view.view_entities.response_aluno import Response_aluno

class Controller_aluno(Controller_base):
    def __init__(self):
        self.model= AlunoService()
        self.view= Response_aluno(self)

    def insert(self, data):
        pass


    def update(self, data):
        pass


    def deleteById(self,id: int):
        pass

 
    def findById(self,id: int):
        pass


    def findAll(self):
        pass