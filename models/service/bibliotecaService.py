from typing import List

from ..model.entities.aluno import Aluno
from ..model.entities.biblioteca import Biblioteca
from ..model.dao.bibliotecaDao import BibliotecaDao
from ..schemas.aluno_schema import Aluno_Schema
from ..schemas.biblioteca_schema import Biblioteca_schema

from ..model.dao.daoFactory import DaoFactory
from .serviceException import ServiceException

class  BibliotecaService(BibliotecaDao):
    def __init__(self):
        super().__init__()
        self.bibliotecaDao= DaoFactory.createBibliotecaDao()

    def insert(self,biblioteca: Biblioteca):
        try:
            return self.bibliotecaDao.insert(biblioteca)
        except Exception as e:
            raise ServiceException(f"Erro ao inserir avalição da biblioteca.\nDetalhes: {e}")

    def update(self,biblioteca: Biblioteca):
        try:
            return self.bibliotecaDao.update(biblioteca)
        except Exception as e:
            raise ServiceException(f"Erro ao atualizar avalição da biblioteca.\nDetalhes: {e}")
            

    def deleteById(self,id: int):
        try:
            return self.bibliotecaDao.deleteById(id)
        except Exception as e:
            raise ServiceException(f"Erro ao deletar avalição da biblioteca com ID {id}.\nDetalhes: {e}")

    def findById(self,id: int):
        try:
            return self.bibliotecaDao.findById(id)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar avalição da biblioteca com ID {id}.\nDetalhes: {e}")

    def findAll(self) -> List[Biblioteca]:
        try:
            return self.bibliotecaDao.findAll()
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos as avalições da biblioteca. \nDetalhes: {e}")

    def findByAluno(self, aluno: Aluno) -> List[Aluno]:
        try:
            return self.bibliotecaDao.findByAluno(aluno)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos as avalições da biblioteca por aluno \nDetalhes: {e}")
        
    def instance_aluno(self, aluno: Aluno_Schema, id= None) -> Aluno:
        try:
            return Aluno(id = id, nome= aluno.nome, sobrenome= aluno.sobrenome)
        except Exception as e:
            raise ServiceException(f"Erro ao instanciar aluno \nDetalhes: {e}")
        
    def instance_biblioteca(self, biblioteca: Biblioteca_schema, id= None) -> Biblioteca:
        try:
            return Biblioteca(id= id, nota= biblioteca.nota, aluno= self.instance_aluno(biblioteca.aluno))
        except Exception as e:
            raise ServiceException(f"Erro ao instanciar biblioteca \nDetalhes: {e}")
    
