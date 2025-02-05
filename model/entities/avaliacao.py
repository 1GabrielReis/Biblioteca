from model.entities.livro import Livro
from model.entities.aluno import Aluno
from model.entities.reserva import Reserva

from typing import List

class Avaliacao:
    def __init__(self, id: int, nota: int, aluno: Aluno, livro: Livro, reserva: Reserva):
        self.id=id
        self.nota=nota
        self.aluno=aluno
        self.livro=livro
        self.reserva=reserva

    def __iter__(self):
        yield self.id
        yield self.nota
        yield self.aluno.nome
        yield self.livro.titutlo
        yield self.reserva.id

    def __str__(self):
        return str(tuple(self.__iter__())) 
        #f'({self.id}, {self.nota}, {self.aluno.nome}, {self.livro.titutlo}, {self.reserva.id})'
    
    def __repr__(self):
        return self.__str__()
    

    # def media(self, notas: List[Avaliacao]):
    #     total= sum(nota.nota for nota in notas)
    #     return total/len(notas)