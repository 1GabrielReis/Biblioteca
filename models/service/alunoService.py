from typing import List

from ..model.entities.aluno import Aluno
from ..model.dao.alunoDao import AlunoDao

from ..schemas.aluno_schema import Aluno_Schema

from ..model.dao.daoFactory import DaoFactory

from .serviceException import ServiceException

class AlunoService(AlunoDao):
    def __init__(self):
        super().__init__()
        self.alunoDao= DaoFactory.createAlunoDao()

    def insert(self,aluno: Aluno):
        try:
            return self.alunoDao.insert(aluno)
        except Exception as e:
            raise ServiceException(f"Erro ao inserir aluno.\nDetalhes: {e}")

    def update(self,aluno: Aluno):
        try:
            return self.alunoDao.update(aluno)
        except Exception as e:
            raise ServiceException(f"Erro ao atualizar aluno.\nDetalhes: {e}")

    def deleteById(self,id: int):
        try:
            return self.alunoDao.deleteById(id)
        except Exception as e:
            raise ServiceException(f"Erro ao deletar aluno com ID {id}.\nDetalhes: {e}")

    def findById(self,id: int):
        try:
            return self.alunoDao.findById(id)
        except Exception as e:
            raise ServiceException(f"Erro ao buscar aluno com ID {id}.\nDetalhes: {e}")
        
    def findAll(self) -> List[Aluno]:
        try:
            alunos= self.alunoDao.findAll()
            return alunos if alunos else []
        except Exception as e:
            raise ServiceException(f"Erro ao buscar todos os alunos. \nDetalhes: {e}")
        
    def instanceObject(self, aluno: Aluno_Schema) -> Aluno:
        return Aluno(id= aluno.id, nome= aluno.nome, sobrenome= aluno.sobrenome)
