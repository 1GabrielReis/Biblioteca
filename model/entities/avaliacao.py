from livro import Livro
from aluno import Aluno
from reserva import Reserva
from avaliacao import Avaliacao

from typing import List

class Avaliacao:
    def __init__(self, id, nota, aluno: Aluno, livro: Livro, reserva: Reserva):
        self.id=id
        self.nota=nota
        self.aluno=aluno
        self.livro=livro
        self.reserva=reserva

    def media(self, notas: List[Avaliacao]):
        total= sum(nota.nota for nota in notas)
        return total/len(notas)