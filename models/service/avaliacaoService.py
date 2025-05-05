from typing import List

from model.entities.aluno import Aluno
from model.entities.livro import Livro
from model.entities.reserva import Reserva
from model.entities.avaliacao import Avaliacao
from model.dao.avaliacaoDao import AvaliacaoDao
from model.dao.daoFactory import DaoFactory

class AvaliacaoService(AvaliacaoDao):
    def __init__(self):
        super().__init__()
        self.avaliacaoDao= DaoFactory.createAvaliacaoDao()
    
    def insert(self,avaliacao: Avaliacao):
        return self.avaliacaoDao.insert(avaliacao)

    def update(self,avaliacao: Avaliacao):
        return self.avaliacaoDao.update(avaliacao)

    def deleteById(self,id: int):
        return self.avaliacaoDao.deleteById(int)

    def findById(self,id: int):
        return self.avaliacaoDao.findById(id)

    def findAll(self) -> List[Avaliacao]:
        return self.avaliacaoDao.findAll()

    def findByAluno(self, avaliacao) -> List[Avaliacao]:
        return self.avaliacaoDao.findByAluno(avaliacao)

    def findByLivro(self, avaliacao) -> List[Avaliacao]:
        return self.avaliacaoDao.findByLivro(avaliacao)

    def findByReserva(self, avaliacao) -> List[Avaliacao]:
        return self.avaliacaoDao.findByReserva(avaliacao)
