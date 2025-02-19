from typing import List

from model.entities.livro import Livro
from model.dao.livroDao import LivroDao

from model.dao.daoFactory import DaoFactory

class LivroService(LivroDao):
    def __init__(self):
        super().__init__()
        self.livroDao= DaoFactory.createLivroDao()

    def insert(self,livro: Livro):
        return self.livroDao.insert(livro)

    def update(self,livro: Livro):
        return self.livroDao.update(livro)

    def deleteById(self,id: int):
        return self.livroDao.deleteById(id)

    def findById(self,id: int):
        return self.livroDao.findById(id)

    def findAll(self) -> List[Livro]:
        return self.livroDao.findAll()