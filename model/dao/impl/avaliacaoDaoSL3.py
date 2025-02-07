from typing import List
import sqlite3 as sql

from model.entities.avaliacao import Avaliacao
from model.dao.avaliacaoDao import AvaliacaoDao

from model.entities.aluno import Aluno
from model.entities.livro import Livro
from model.entities.reserva import Reserva

from db.db import DB
from db.dbException import DbException

class AvaliacaoDaoSL3(AvaliacaoDao):
    def __init__(self, conn):
        super().__init__()
        self.conn= conn

    def insert(self,avaliacao: Avaliacao):
        pass

    def update(self,avaliacao: Avaliacao):
        pass

    def deleteById(self,id: int):
        pass

    def findById(self,id: int):
        pass

    def findAll(self) -> List[Avaliacao]:
        pass

    def findByAluno(self, avaliacao) -> List[Avaliacao]:
        pass

    def findByLivro(self, avaliacao) -> List[Avaliacao]:
        pass

    def findByReserva(self, avaliacao) -> List[Avaliacao]:
        pass
