from typing import List
from datetime import datetime

from model.entities.aluno import Aluno
from model.entities.livro import Livro
from model.entities.reserva import Reserva
from model.dao.reservaDao import ReservaDao

from model.dao.daoFactory import DaoFactory

class ReservaService(ReservaDao):
    def __init__(self):
        super().__init__()
        self.reservaDao= DaoFactory.createReservaDao()

    def insert(self,reserva: Reserva):
        return self.reservaDao.insert(reserva)

    def update(self,reserva: Reserva):
        return self.reservaDao.update(reserva)

    def deleteById(self,id: int):
        return self.reservaDao.deleteById(id)

    def findById(self,id: int):
        return self.reservaDao.findById(id)

    def findAll(self) -> List[Reserva]:
        return self.reservaDao.findAll()

    def findByLivro(self, livro: Livro) -> List[Livro]:
        return self.reservaDao.findByLivro(livro)

    def findByAluno(self, aluno: Aluno) -> List[Aluno]:
        return self.reservaDao.findByAluno(aluno)

    def returnBook(self, reserva: Reserva):
        return self.reservaDao.returnBook(reserva)