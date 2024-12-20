from datetime import datetime

from model.entities.livro import Livro
from model.entities.aluno import Aluno

class Reserva:
    def __init__(self, id,livro: Livro, aluno: Aluno, data_inicio: datetime, data_final: datetime, data_entregue: datetime):
        self.id=id
        self.livro= livro 
        self.aluno= aluno 
        self.data_inicio=data_inicio
        self.data_final=data_final
        self.data_entregue=data_entregue

    def __str__(self):
        return f'''
        ({self.id}, {self._formataData(self.data_inicio)}, {self._formataData(self.data_final)}, {self._formataData(self.data_final)}, {self.livro.id}, {self.livro.titutlo}, {self.aluno.id}, {self.aluno.nome})
        '''
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def _formataData(self, data:datetime) -> str:
        return data.strftime(" %d/ %m /%Y ")