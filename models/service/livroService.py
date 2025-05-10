from typing import List

from ..model.entities.livro import Livro
from ..model.dao.livroDao import LivroDao
from ..model.dao.daoFactory import DaoFactory

from ..schemas.livro_schema import Livro_Schema

from ..service.serviceException import ServiceException

class LivroService(LivroDao):
    def __init__(self):
        super().__init__()
        self.livroDao= DaoFactory.createLivroDao()

    def insert(self,livro: Livro):
        try:
            return self.livroDao.insert(livro)
        except Exception as e:
            raise ServiceException(f"Erro ao inserir livro.\nDetalhes: {e}")

    def update(self,livro: Livro):
        try:
            return self.livroDao.update(livro)
        except Exception as e:
            raise ServiceException(f"Erro ao atualizar livro.\nDetalhes: {e}")

    def deleteById(self,id: int):
        try:
            return self.livroDao.deleteById(id)
        except Exception as e:
            raise ServiceException(f"Erro ao deletar livro com ID {id}.\nDetalhes: {e}")

    def findById(self,id: int):
        try:
            return self.livroDao.findById(id)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar livro com ID {id}.\nDetalhes: {e}")

    def findAll(self) -> List[Livro]:
        try:
            return self.livroDao.findAll()
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos os livros. \nDetalhes: {e}")
        
    def instanceObject(self, livro: Livro_Schema, id= None) -> Livro:
        try:
            return livro(id= id, titulo= livro.titulo, autor= livro.autor, editora= livro.editora)
        except Exception as e:
            raise ServiceException(f"Erro ao instância livro \nDetalhes: {e}")