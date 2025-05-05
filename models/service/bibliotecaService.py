from typing import List

from model.entities.aluno import Aluno
from model.entities.biblioteca import Biblioteca
from model.dao.bibliotecaDao import BibliotecaDao

from model.dao.daoFactory import DaoFactory

class  BibliotecaService(BibliotecaDao):
    def __init__(self):
        super().__init__()
        self.bibliotecaDao= DaoFactory.createBibliotecaDao()

    def insert(self,biblioteca: Biblioteca):
        return self.bibliotecaDao.insert(biblioteca)

    def update(self,biblioteca: Biblioteca):
        return self.bibliotecaDao.update(biblioteca)

    def deleteById(self,id: int):
        return self.bibliotecaDao.deleteById(id)

    def findById(self,id: int):
        return self.bibliotecaDao.findById(id)

    def findAll(self) -> List[Biblioteca]:
        return self.bibliotecaDao.findAll()

    def findByAluno(self, aluno: Aluno) -> List[Aluno]:
        return self.bibliotecaDao.findByAluno(aluno)