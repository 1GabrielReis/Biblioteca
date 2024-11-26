import datetime

from .livro import Livro
from .aluno import Aluno

class Reserva:
    def __init__(self, id,livro: Livro, aluno: Aluno, data_inicio: datetime, data_final: datetime, data_entregue: datetime):
        self.id=id
        self.livro= livro 
        self.aluno= aluno 
        self.data_inicio=data_inicio
        self.data_final=data_final
        self.data_entregue=data_entregue

    